from django.contrib import admin
from main.models import Customer, Book, Order

class OrderAdmin(admin.ModelAdmin):
#    exclude = ('order_number',)
    date_hierarchy = 'order_date'
    list_display = ('order_number', 'order_date', 'customer', 'book')
    list_filter = ('order_date', 'book')
    ordering = ('order_date',)
    search_fields = ['^order_number', '^customer__name', '^customer__email']

class OrderInLine(admin.TabularInline):
    model = Order
    exclude = ('order_number',)
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email')
    ordering = ('name',)
    search_fields = ['^name', '^email', 'tel']
    inlines = (OrderInLine,)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Book)
admin.site.register(Order, OrderAdmin)