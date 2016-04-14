# -*- coding: utf-8 -*-

from models import User

from flask.ext.wtf import Form
from wtforms.widgets import TextInput
from wtforms_alchemy import model_form_factory
from wtforms import PasswordField, StringField
from wtforms.validators import Email

BaseModelForm = model_form_factory(Form)

class BootstrapInputWidgetMixin(object):
    """Adds the field's name as a class
    when subclassed with any WTForms Field type.

    Has not been tested - may not work."""
    def __init__(self, *args, **kwargs):
        super(BootstrapInputWidgetMixin, self).__init__(*args, **kwargs)

    def __call__(self, field, **kwargs):
        c = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = u'%s %s' % (field.short_name, c)
        # kwargs['class'] = u'form-control'
        return super(BootstrapInputWidgetMixin, self).__call__(field, **kwargs)

# An example
class ClassedTextInput(BootstrapInputWidgetMixin, TextInput):
        pass

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
        validators = {
            'email': [Email()],
        }