#-*-encoding:utf-8-*-
from django.db import models
from django.conf import settings
import datetime

DELIVERY_METHODS = (
    ('pickup', u'самовывоз'),
    ('courier', u'курьер'),
#    ('post', u'почта')
)

PAYMENT_METHODS = (
    ('cash', u'наличные'),
#    ('yandex', u'Яндекс.Деньги'),
)
class Customer(models.Model):
#    lastname = models.CharField(u"Фамилия", max_length=200)
#    firstname = models.CharField(u"Имя", max_length=200)
    name = models.CharField(u'Имя', max_length=200)
    email = models.EmailField("E-mail")
    tel = models.CharField(u"Телефон", max_length=20)
    city = models.CharField(u"Город", max_length=200, default=u'')
    address = models.CharField(u"Адрес", max_length=250, default=u'')

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.email)

    class Meta:
        verbose_name = u'Покупатель'
        verbose_name_plural = u'Покупатели'

class Book(models.Model):
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(u'Цена', max_digits=9, decimal_places=2)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', verbose_name=u'Покупатель')
    book = models.ForeignKey(Book, verbose_name=u'Книга')
    quantity = models.PositiveIntegerField(u"Количество")
    payment_method = models.CharField(u"Форма оплаты", max_length=200, choices=PAYMENT_METHODS)
    delivery_method = models.CharField(u"Вид доставки", max_length=200, choices=DELIVERY_METHODS)
    delivery_price = models.DecimalField(u"Стоимость доставки", max_digits=9, decimal_places=2, default=0)
    order_date = models.DateTimeField(u'Дата заказа')
    order_number = models.CharField(u'Номер заказа', max_length=20)
    amount = models.DecimalField(u'Стоимость', max_digits=9, decimal_places=2)

    def calc_total(self):
        return self.quantity * self.book.price + self.delivery_price

    @classmethod
    def calc_total2(cls, quantity=0, price=0, delivery_price=0):
        return quantity * price + delivery_price
    
    def __unicode__(self):
        return u"Заказ №%s" % self.order_number

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.book.price
        self.check_order_number()
        return super(Order, self).save(*args, **kwargs)

    def check_order_number(self):
        incr = 1
        while True:
            order_number = Order.objects.filter(order_number=self.order_number)
            if order_number:
                self.order_number = self.calc_order_number(incr)
                incr += 1
            else:
                break

    def calc_order_number(self, incr=None):
        if not self.order_date:
            self.order_date = datetime.datetime.now()
        order_number = u"%s%s от %s" % (
            self.order_date.strftime('%H%M'),
            (incr or ""),
            self.order_date.strftime('%d.%m.%y'))
        return order_number

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'