# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, validators, ValidationError


def full_name_validator(form, field):
    name_parts = field.data.split(' ')
    if len(name_parts) < 2:
        raise ValidationError('You must enter name and surname with spaces!')


class BlogPostForm(Form):
    author = StringField(label='Author', validators=[
        validators.Length(min=4, max=100),
    ])
    title = StringField(label='Title', validators=[
        validators.Length(min=3, max=30)
    ])
    text = StringField(label='Text', validators=[
        validators.Length(min=5, max=200),
    ])
