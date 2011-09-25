#-*-encoding:utf-8-*-
from django.db import models

DELIVERY_METHODS = (
    ('pickup', u'самовывоз'),
    ('courier', u'курьер'),
    ('post', u'почта')
)
class Customer(models.Model):
    lastname = models.CharField(u"Фамилия", max_length=200)
    firstname = models.CharField(u"Имя", max_length=200)
    email = models.EmailField("E-mail")
    tel = models.CharField(u"Телефон", max_length=20)

    def __unicode__(self):
        return " ".join((self.lastname, self.firstname))

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    book = models.ForeignKey(Book)
    quantity = models.PositiveIntegerField(u"Количество")
    payment_method = models.CharField(u"Форма оплаты", max_length=200)
    delivery_method = models.CharField(u"Вид доставки", max_length=200, choices=DELIVERY_METHODS)