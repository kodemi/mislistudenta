from django.forms import ModelForm
from main.models import Customer

class OrderForm(ModelForm):
    class Meta:
        model = Customer