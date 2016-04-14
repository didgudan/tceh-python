# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

import config

__author__ = 'sobolevn'


login_manager = LoginManager()
db = SQLAlchemy()


@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(user_id)


def create_app():
    from views import auth

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config)

    # Blueprints:
    app.register_blueprint(auth)

    # Custom modules:
    login_manager.init_app(app)
    # login_manager.login_view = 'auth.login'
    db.init_app(app)

    # Dynamic context:
    with app.app_context():
        db.create_all()

    return app


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))
    # return 'Unauthorized', 401


if __name__ == '__main__':
    app = create_app()
    app.run()

