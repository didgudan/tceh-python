# -*- coding: utf-8 -*-

from flask import Flask, current_app, Blueprint
from flask_sqlalchemy import SQLAlchemy

__author__ = 'sobolevn'


views = Blueprint('views', __name__, url_prefix='/')
db = SQLAlchemy()  # note, no app passed.


@views.route('/')
def index():
    return current_app.config['DEFAULT_RESPONSE']


def create_app():
    app = Flask(__name__)
    app.config.update({
        'DEBUG': True,
        'DEFAULT_RESPONSE': 'hello, world!',
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    })
    # else:
        # app.config.from_object(test_config)

    # Do some extra init:
    app.register_blueprint(views)  # (import views in real life)
    db.init_app(app)  # now SQLAlchemy is inited.

    return app


if __name__ == '__main__':
    # current_app.run()
    app = create_app()
    app.run()
