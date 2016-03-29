# -*- coding: utf-8 -*-

import datetime
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from flask.ext.login import UserMixin

from app import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(30))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return '%s' % self.username

    def __str__(self):
        return repr(self)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(
        'User', backref=db.backref('posts', lazy='dynamic')
    )

    title = db.Column(db.String(140), unique=True)
    content = db.Column(db.String(3000))

    date_created = db.Column(db.Date, default=datetime.date.today())
    is_visible = db.Column(db.Boolean, default=True)

    def __init__(self, title='', content='', user=None,
                 date_created=None, is_visible=None):
        self.title = title
        self.content = content
        self.user = user

        if date_created is not None:
            self.date_created = date_created

        if is_visible is not None:
            self.is_visible = is_visible
