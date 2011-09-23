#-*-encoding:utf-8-*-

from django.forms import ModelForm, TextInput, Select
from main.models import Customer

verbose_name = lambda field_name: Customer._meta.get_field_by_name(field_name)[0].verbose_name

class OrderForm(ModelForm):
    class Meta:
        model = Customer
        widgets = {
            'lastname': TextInput(attrs={'class': 'span3'}),
            'firstname': TextInput(attrs={'class': 'span3'}),
            'email': TextInput(attrs={'class': 'span3 validate[required,custom[email]]'}),
            'tel': TextInput(attrs={'class': 'span3'}),
            'quantity': TextInput(attrs={'class': 'span3'}),
            'payment_method': TextInput(attrs={'class': 'span3'}),
            'delivery_method': Select(attrs={'class': 'span3'}),
        }

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