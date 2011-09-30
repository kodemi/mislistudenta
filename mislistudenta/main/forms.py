#-*-encoding:utf-8-*-
from django import forms
from django.forms import ModelForm, TextInput, Select, HiddenInput
from main.models import Customer, Book, Order

verbose_name = lambda model, field_name: model._meta.get_field_by_name(field_name)[0].verbose_name

class OrderForm(forms.Form):
#    lastname = forms.CharField(
#            max_length=200,
#            label=verbose_name(Customer, 'lastname'),
#            widget=TextInput(attrs={'class': 'span4 validate[required,custom[onlyLetterSp]]'}))
#    firstname = forms.CharField(
#            max_length=200,
#            label=verbose_name(Customer, 'firstname'),
#            widget=TextInput(attrs={'class': 'span4 validate[required,custom[onlyLetterSp]]'}))
    name = forms.CharField(
            max_length=200,
            label=verbose_name(Customer, 'name'),
            widget=TextInput(attrs={'class': 'span4 validate[required,custom[onlyLetterSp]]'}))
    email = forms.EmailField(
            label=verbose_name(Customer, 'email'),
            widget=TextInput(attrs={'class': 'span4 validate[required,custom[email]]'}))
    tel = forms.CharField(
            max_length=20,
            label=verbose_name(Customer, 'tel'),
            widget=TextInput(attrs={'class': 'span4 validate[required,custom[phone]]'}))
    quantity = forms.IntegerField(
            label=verbose_name(Order, 'quantity'),
            widget=TextInput(attrs={'class': 'span4 validate[required,min[1],max[100],custom[integer]'}))
    payment_method = forms.ChoiceField(
            label=verbose_name(Order, 'payment_method'),
            widget=Select(attrs={'class': 'span4 validate[required]'}),
            choices=Order._meta.get_field_by_name('payment_method')[0].choices)
    delivery_method = forms.ChoiceField(
            label=verbose_name(Order, 'delivery_method'),
            widget=Select(attrs={'class': 'span4 validate[required]'}),
            choices=Order._meta.get_field_by_name('delivery_method')[0].choices)
    book = forms.CharField(
            max_length=200,
            label=u"Ежедневник",
            widget=HiddenInput())
