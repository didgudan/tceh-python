# -*- coding: utf-8 -*-

import random
import string

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__author__ = 'sobolevn'


app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
})
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   index=True)
    name = db.Column(db.String(100), unique=True, index=True)
    tag = db.Column(db.String(5), index=True)

    def __init__(self, name, tag):
        self.name = name
        self.tag = tag


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True,
                   index=True)

    title = db.Column(db.String(150), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        index=True)  # now let's test it.
    user = db.relationship(
        'User', backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title, user=None):
        self.title = title
        self.user = user


class UserWithoutIndexes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    tag = db.Column(db.String(5))

    def __init__(self, name, tag):
        self.name = name
        self.tag = tag


class PostWithoutIndexes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150))

    user_id = db.Column(db.Integer, db.ForeignKey('user_without_indexes.id'))
    user = db.relationship(
        'UserWithoutIndexes', backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title, user=None):
        self.title = title
        self.user = user


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for _ in range(length))


def query_and_time(klass, **kwargs):
    select_start = time.clock()
    for _ in range(10000):
        db.session.query(User).filter_by(**kwargs).all()
    print('timing for %s result is %s', (
        klass.__name__, time.clock() - select_start))


if __name__ == '__main__':
    import time

    db.create_all()

    if not User.query.count() and not Post.query.count():
        for i in range(10000):
            tag = random_string(5)
            user = User('user' + str(i), tag)
            db.session.add(user)

            title = random_string(50)
            post = Post(title, user=user)
            db.session.add(post)
            # db.session.commit()
        db.session.commit()

    if not UserWithoutIndexes.query.count() \
            and not PostWithoutIndexes.query.count():
        for i in range(10000):
            tag = random_string(5)
            user = UserWithoutIndexes('userWOI' + str(i), tag)
            db.session.add(user)

            title = random_string(50)
            post = PostWithoutIndexes(title, user=user)
            db.session.add(post)
        db.session.commit()

    query_and_time(User, name='some_name')
    query_and_time(UserWithoutIndexes, name='some_name')



