# -*- coding: utf-8 -*-

from models import User

from flask.ext.wtf import Form
from wtforms_alchemy import model_form_factory
from wtforms import PasswordField, StringField
from wtforms.validators import Email

BaseModelForm = model_form_factory(Form)

def passwords_match(form, field):
    if form.password.data != field.data:
        raise ValueError('Passwords do not match')


class LoginForm(Form):
    username = StringField()
    password = PasswordField()


class RegisterForm(BaseModelForm):
    password = PasswordField()
    repeat_password = PasswordField(validators=[
        passwords_match,
    ])

    class Meta:
        model = User
        # exclude = ['registered_on']
        validators = {
            'email': [Email()],
        }