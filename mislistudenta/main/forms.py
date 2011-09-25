#-*-encoding:utf-8-*-
from django import forms
from django.forms import ModelForm, TextInput, Select
from main.models import Customer, Book, Order

verbose_name = lambda model, field_name: model._meta.get_field_by_name(field_name)[0].verbose_name

#class OrderForm(ModelForm):
#    class Meta:
#        model = Customer
#        widgets = {
#            'lastname': TextInput(attrs={'class': 'span3 validate[required,custom[onlyLetterSp]]'}),
#            'firstname': TextInput(attrs={'class': 'span3 validate[required,custom[onlyLetterSp]]'}),
#            'email': TextInput(attrs={'class': 'span3 validate[required,custom[email]]'}),
#            'tel': TextInput(attrs={'class': 'span3 validate[required,custom[phone]]'}),
#            'quantity': TextInput(attrs={'class': 'span3 validate[required,min[1],custom[integer]'}),
#            'payment_method': TextInput(attrs={'class': 'span3 validate[required]'}),
#            'delivery_method': Select(attrs={'class': 'span3 validate[required]'}),
#        }

class OrderForm(forms.Form):
    lastname = forms.CharField(max_length=200,
                               label=verbose_name(Customer, 'lastname'),
                               widget=)
    firstname = forms.CharField(max_length=200, label=verbose_name(Customer, 'firstname'))
    email = forms.EmailField(label=verbose_name(Customer, 'email'))
    tel = forms.CharField(max_length=20, label=verbose_name(Customer, 'tel'))
    quantity = forms.IntegerField(label=verbose_name(Order, 'quantity'))
    payment_method = forms.CharField(max_length=200, label=verbose_name(Order, 'payment_method'))
    delivery_method = forms.ChoiceField(
        choices=Order._meta.get_field_by_name('delivery_method')[0].choices,
        label=verbose_name(Order, 'delivery_method'))

class CheckOrderForm(ModelForm):
    class Meta:
        model = Customer
        widgets = {
            'lastname': TextInput(attrs={'class': 'span5'}),
            'firstname': TextInput(attrs={'class': 'span5'}),
            'email': TextInput(attrs={'class': 'span5'}),
            'tel': TextInput(attrs={'class': 'span5'}),
            'quantity': TextInput(attrs={'class': 'span5'}),
            'payment_method': TextInput(attrs={'class': 'span5'}),
            'delivery_method': Select(attrs={'class': 'span5'}),
        }