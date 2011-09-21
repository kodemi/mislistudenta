#-*-encoding:utf-8-*-
from django.db import models

DELIVERY_METHODS = (
    ('pickup', u'самовывоз'),
    ('courier', u'курьер'),
    ('post', u'почта')
)
class Customer(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=200)
    delivery_method = models.CharField(max_length=200, choices=DELIVERY_METHODS)

    def __unicode__(self):
        return " ".join((self.lastname, self.firstname))