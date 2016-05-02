
from django.db import models

class User(models.Model):
    name = models.CharField()
    surname = models.CharField()
    email = models.EmailField()
    password = models.PasswordField()
    login_name = models.CharField()

class Project(models.Model):
    name = models.CharField()
    author = models.ManyToManyField('User')

class Issue(models.Model):
    name = models.CharField()
    author = models.ForeignKey('User')
    text = models
    requirement = models.ForeignKey('Requirement')

class Tag(models.Model):
    name = models.CharField()

class Level(models.Model):
    name = models.CharField()

class Requirement(models.Model):
    tag = models.ForeignKey('Tag')
    level = models.ForeignKey('Level')
    full_name = tag + level
    issue = models.ForeignKey('Issue')

class Assistant(models.Model):
    user = models.CharField()
    requirement = models.ForeignKey('Requirement')