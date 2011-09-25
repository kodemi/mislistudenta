from django.contrib import admin
from main.models import Customer, Book, Order

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)