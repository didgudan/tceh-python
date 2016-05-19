from __future__ import unicode_literals

from django.db import models


class Lesson(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=40)

    def __unicode__(self):
        return "Lesson number %s (%s)" % (self.number, self.title)


class Theme(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    lesson = models.ForeignKey('Lesson', related_name='theme', blank=True,
                               null=True)

    def __unicode__(self):
        return "Theme: %s" % self.name
