from __future__ import unicode_literals
import os

from django.conf import settings
from django.db import models
from django.db.models import Manager
from django.utils import timezone
from django.db.models.signals import post_save
from django.utils.text import get_valid_filename


class Address(models.Model):
    # city = models.ForeignKey('City', related_name='addresses')
    user = models.ForeignKey('auth_app.CustomUser')
    full = models.CharField(max_length=150)

    def __unicode__(self):
        return unicode(self.full)


class PizzaIngredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']


class PizzaMenuItem(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(
        'PizzaIngredient', related_name='ingredients')

    def __unicode__(self):
        return unicode(self.name)


class PizzaSize(models.Model):
    size = models.CharField(max_length=5)
    full_name = models.CharField(max_length=25)
    order_number = models.IntegerField()

    def __unicode__(self):
        return unicode(self.size)

    class Meta:
        ordering = ['order_number']

class PizzaOrderManager(Manager):
    def get_queryset(self, **kwargs):
        return super(PizzaOrderManager, self).get_queryset().filter(
            delivered=True,
        )


class PizzaOrder(models.Model):
    kind = models.ForeignKey('PizzaMenuItem', related_name='pizzas')
    size = models.ForeignKey('PizzaSize', related_name='pizzas')
    delivery = models.ForeignKey('Address', related_name='pizzas')

    extra = models.ManyToManyField(
        'PizzaIngredient', blank=True, related_name='pizzas_extras')
    exclude = models.ManyToManyField('PizzaIngredient', blank=True)
    comment = models.CharField(max_length=140, blank=True)

    delivered = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_delivered = models.DateTimeField(default=None, blank=True, null=True)

    objects = Manager()
    delivered_manager = PizzaOrderManager()

    def mark_delivered(self, commit=True):
        """
        Ths method changes state of pizza order.
        :param commit:
        :return:
        """
        self.delivered = True
        self.date_delivered = timezone.now()
        if commit:
            self.save()

    def save(self, **kwargs):
        if not self.pk:
            print('Creating new PizzaOrder!')
        else:
            print('Updating the existing one')

        super(PizzaOrder, self).save(**kwargs)

    def __unicode__(self):
        return u'PizzaOrder [%s]' % self.id

    class Meta:
        ordering = ['-delivered']


def content_filename(instance, filename):
    return os.path.join(
        settings.MEDIA_ROOT,
        'auth_app',
        'files',
        get_valid_filename(type(instance).__name__.lower()),
        get_valid_filename(filename),
    )


class PizzaOrderPhoto(models.Model):
    class Meta:
        abstract = True

    order = models.ForeignKey('PizzaOrder')
    image = models.ImageField(upload_to=content_filename)


class CookingPizza(PizzaOrderPhoto):
    started = models.DateTimeField(default=timezone.now)
    finished = models.DateTimeField(default=None, null=True)


class DeliveredPizza(PizzaOrderPhoto):
    courier_name = models.CharField(max_length=50)


def post_save_handler(sender, **kwargs):
    print(sender, kwargs)
    print('The order was updated! Notify everyone!')


post_save.connect(post_save_handler, sender=PizzaOrder)
