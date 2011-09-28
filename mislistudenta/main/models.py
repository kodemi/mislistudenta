#-*-encoding:utf-8-*-
from django.db import models

DELIVERY_METHODS = (
    ('pickup', u'самовывоз'),
    ('courier', u'курьер'),
    ('post', u'почта')
)

PAYMENT_METHODS = (
    ('cash', u'наличные'),
    ('yandex', u'Яндекс.Деньги'),
)
class Customer(models.Model):
    lastname = models.CharField(u"Фамилия", max_length=200)
    firstname = models.CharField(u"Имя", max_length=200)
    email = models.EmailField("E-mail")
    tel = models.CharField(u"Телефон", max_length=20)

    def __unicode__(self):
        return u" ".join((self.lastname, self.firstname))

    class Meta:
        verbose_name = u'Покупатель'
        verbose_name_plural = u'Покупатели'

class Book(models.Model):
    title = models.CharField(max_length=200)
    alias = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(u'Цена', max_digits=9, decimal_places=2)

    def __unicode__(self):
        return u"%s (%s)" % (self.title, self.alias)

    class Meta:
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', verbose_name=u'Покупатель')
    book = models.ForeignKey(Book, verbose_name='Книга')
    quantity = models.PositiveIntegerField(u"Количество")
    payment_method = models.CharField(u"Форма оплаты", max_length=200, choices=PAYMENT_METHODS)
    delivery_method = models.CharField(u"Вид доставки", max_length=200, choices=DELIVERY_METHODS)
    order_date = models.DateTimeField(u'Дата заказа')
    order_number = models.CharField(u'Номер заказа', max_length=6)
    amount = models.DecimalField(u'Стоимость', max_digits=9, decimal_places=2)

    def __unicode__(self):
        return u"Заказ №%s" % self.order_number

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.book.price
        return super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'