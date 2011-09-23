from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.context_processors import csrf
from main.forms import OrderForm, CheckOrderForm
from django.utils import simplejson

def home(request):
    context = {}
    context['order_form'] = OrderForm()
    context['check_order_form'] = CheckOrderForm()
    context.update(csrf(request))
    return render_to_response("main/home.html", context)

def order(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            print "ololo"
            #Do Something, e.g. save, send an email
            template = "main/success.html"
            success = True
        else:
            template = "main/order_form.html"
            context["order_form"] = form
            success = False
    else:
        template = "main/order_form.html"
        context["order_form"] = OrderForm()
        success = False
    html = render_to_string(template, context)
    print html
    response = simplejson.dumps({"success": success, "html": html})
    return HttpResponse(response,
                        content_type=\
                            "application/javascript; charset=utf-8")