# -*- coding: utf-8 -*-

from datetime import datetime

from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

from app import db

__author__ = 'sobolevn'


class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)

    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(10))
    email = db.Column('email', db.String(50), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)

    def __init__(self, username=None, email=None):
        self.username = username
        # we do not store original password.
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %s>' % self.username
