# -*- coding: utf-8 -*-

from datetime import datetime

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


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(40), index=True)

    def __init__(self, content):
        self.content = content


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), index=True)

    def __init__(self, title):
        self.title = title

if __name__ == '__main__':
    db.create_all()

    try:
        event_title = 'server started'
        event = Event(event_title)

        event.title += 'a'
        db.session.add(event)

        log = Log('{} {}'.format(event_title, datetime.utcnow()))
        db.session.add(log)

        raise ValueError('The error happened')

        db.session.commit()
    except Exception as ex:
        print(ex)
        db.session.rollback()

    # engine = db.get_engine(app)
    # http://docs.sqlalchemy.org/en/rel_0_9/core/connections.html#using-transactions
