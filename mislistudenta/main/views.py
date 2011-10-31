#-*-encoding:utf-8-*-
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.context_processors import csrf
from main.forms import OrderForm
from main.models import Customer, Order, Book
from django.utils import simplejson
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings
import datetime
from urlparse import parse_qsl
from urllib2 import unquote
from decimal import Decimal


def home(request):
    context = {}
    try:
        context['white_price'] = Book.objects.get(alias='white').price
        context['red_price'] = Book.objects.get(alias='red').price
        now = datetime.datetime.now()
        today = datetime.date(year=now.year, month=now.month, day=now.day)
        context['today'] = today
        today_orders = Order.objects.filter(
            order_date__gte=today).order_by(
            '-order_date')
        context['last_order_number'] = today_orders and today_orders[0].order_number.split()[0]
    except ObjectDoesNotExist:
        pass
#    context['order_form'] = OrderForm()
    template = settings.MAIN_TEMPLATE
    return render(request, template, context)

def order(request):
    context = {}
    context.update(csrf(request))
    template = "main/order_dialog_step1.html"
    if request.method == 'POST':
        step = request.POST.get('step', '1')
        form = OrderForm(request.POST)
        if form and form.is_valid():
            if step == '1': # form -> preview
                try:
                    book = Book.objects.get(alias=form.cleaned_data['book'])
                except ObjectDoesNotExist:
                    response = simplejson.dumps({"success": False})
                    return HttpResponse(response,
                        content_type="application/javascript; charset=utf-8")
                context['book'] = book
                context['check_form'] = form
                context['total'] = Order.calc_total2(
                    quantity=form.cleaned_data['quantity'],
                    price=Book.objects.filter(alias="red")[0].price,
                    delivery_price=Decimal(settings.DELIVERY_PRICE)
                        if form.cleaned_data['delivery_method'] == 'courier' else 0)
                template = "main/order_dialog_step2.html"
                success = True
            elif step == '2': # preview -> submit
                success = True
                customer = Customer()
                order = Order()
#                customer.lastname = form.cleaned_data['lastname']
#                customer.firstname = form.cleaned_data['firstname']
                customer.name = form.cleaned_data['name']
                customer.email = form.cleaned_data['email']
                customer.tel = form.cleaned_data['tel']
                customer.city = form.cleaned_data['city']
                customer.address = form.cleaned_data['address']
                customer.save()
                order.book = Book.objects.get(alias=form.cleaned_data['book'])
                order.quantity = form.cleaned_data['quantity']
                order.payment_method = form.cleaned_data['payment_method']
                order.delivery_method = form.cleaned_data['delivery_method']
                if order.delivery_method == 'courier':
                    order.delivery_price = Decimal(settings.DELIVERY_PRICE)
                order.order_date = datetime.datetime.now()
                order.order_number = order.calc_order_number()
                order.customer = customer
                order.save()
                context['order'] = order
                context['total'] = order.calc_total()
                template = "main/order_dialog_finish.html"
                email_html_content = render_to_string('main/confirmation.html', RequestContext(request, context))
                email_text_content = strip_tags(email_html_content)
                for destination in [order.customer.email, settings.DELIVERY_EMAIL]:
                    msg = EmailMultiAlternatives(u'Заказ на mislistudenta.ru', email_text_content, "mislistudenta.ru <%s>" % settings.EMAIL_HOST_USER, [destination])
                    msg.attach_alternative(email_html_content, 'text/html')
                    msg.send()
        else:
            form._errors = {}
            context["order_form"] = form
            success = False
    else:
        form = request.GET.get('form')
        if form:
            form = unquote(request.GET.get('form').encode('utf8')).decode('utf8')
            context["order_form"] = OrderForm(initial=dict(parse_qsl(form)))
        else:
            context["order_form"] = OrderForm()
        context['delivery_price'] = settings.DELIVERY_PRICE
        success = True
    html = render_to_string(template, RequestContext(request, context))
    response = simplejson.dumps({"success": success, "html": html})
    return HttpResponse(response,
                        content_type="application/javascript; charset=utf-8")

def contacts(request):
    return render(request, "main/contacts.html", {})

def subscribe(request, order_number):
    print order_number
    if request.method == 'POST':
        subscribed = request.POST.get('subscribed', True)
        order = Order.objects.filter(order_number=order_number)
        if order:
            customer = order[0].customer
            customer.subscribe = True if subscribed == 'true' else False
            customer.save()
        response = ""
        return HttpResponse(response,
                        content_type="application/javascript; charset=utf-8")
    return HttpResponse("",
                        content_type="application/javascript; charset=utf-8")