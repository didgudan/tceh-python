# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, validators, ValidationError


def full_name_validator(form, field):
    name_parts = field.data.split(' ')
    if len(name_parts) < 2:
        raise ValidationError('You must enter name and surname with spaces!')

# def API_validator(form, field):
#     try:



class APIForm(Form):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=100), full_name_validator
    ])
    email = StringField(label='Email', validators=[
        validators.Length(min=3, max=30), validators.Email()
    ])