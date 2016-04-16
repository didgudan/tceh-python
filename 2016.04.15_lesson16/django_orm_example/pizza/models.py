from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, m2m_changed


class Address(models.Model):
    # city = models.ForeignKey('City', related_name='addresses')
    full = models.CharField(max_length=150)

    def __unicode__(self):
        return unicode(self.full)


class PizzaIngredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)


class PizzaMenuItem(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(
        'PizzaIngredient', related_name='ingredients')

    def __unicode__(self):
        return unicode(self.name)


class PizzaSize(models.Model):
    LARGE = ('XL', 'XL')
    MEDIUM = ('MD', 'MD')
    SMALL = ('SM', 'SM')
    __all = (LARGE, MEDIUM, SMALL)

    size = models.CharField(max_length=2, choices=__all)

    def __unicode__(self):
        return unicode(self.size)


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
    date_delivered = models.DateTimeField(default=None, null=True)

    def mark_delivered(self, commit=True):
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


def post_save_handler(sender, **kwargs):
    print(sender, kwargs)
    print('The order was updated! Notify everyone!')


post_save.connect(post_save_handler, sender=PizzaOrder)
