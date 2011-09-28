#-*-encoding:utf-8-*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.context_processors import csrf
from main.forms import OrderForm
from main.models import Customer, Order, Book
from django.utils import simplejson
from django.core.mail import send_mail
from django.conf import settings
import datetime
from urlparse import parse_qsl

def home(request):
    context = {}
    context['order_form'] = OrderForm()
#    context.update(csrf(request))
    return render(request, "main/home.html", context)

def order(request):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        #step = request.POST.get('step', '1')
        #form_data = dict(parse_qsl(request.POST.get('form', '')))
        #step = form_data and form_data.get('step', '1')
        step = request.POST.get('step', '1')
        if step == '1':
            form = OrderForm(request.POST)
            if form and form.is_valid():
                context['check_form'] = form
                template = "main/order_dialog_step2.html"
                success = True
            else:
                template = "main/order_dialog_step1.html"
                form._errors = {}
                context["order_form"] = form
                success = False
        elif step == '2':
            print 'step2'
            form = OrderForm(request.POST)
            if form and form.is_valid():
                print 'valid'
                customer = Customer()
                order = Order()
                customer.lastname = form.cleaned_data['lastname']
                customer.firstname = form.cleaned_data['firstname']
                customer.email = form.cleaned_data['email']
                customer.tel = form.cleaned_data['tel']
                customer.save()
                order.book = Book.objects.filter(alias='red')[0]
                order.quantity = form.cleaned_data['quantity']
                order.payment_method = form.cleaned_data['payment_method']
                order.delivery_method = form.cleaned_data['delivery_method']
                order.order_date = datetime.datetime.now()
                order.order_number = "%02d%02d%02d" % (
                    order.order_date.day,
                    order.order_date.hour,
                    order.order_date.minute)
                order.customer = customer
                order.save()
                context['order'] = order
                template = "main/order_dialog_finish.html"
                success = True
                send_mail(u'Заказ на mislistudenta.ru', render_to_string('main/confirmation.txt', context), settings.EMAIL_HOST_USER, [order.customer.email])
    else:
        template = "main/order_dialog_step1.html"
        form = request.GET.get('form')
        print form
        if form:
            context["order_form"] = OrderForm(initial=dict(parse_qsl(form)))
        else:
            context["order_form"] = OrderForm()
        success = True
    html = render_to_string(template, context)
#    print html
    response = simplejson.dumps({"success": success, "html": html})
    return HttpResponse(response,
                        content_type="application/javascript; charset=utf-8")