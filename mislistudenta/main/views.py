from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from main.forms import OrderForm

def home(request):
    context = {}
    context['form'] = OrderForm()
    context.update(csrf(request))
    return render_to_response("main/home.html", context)