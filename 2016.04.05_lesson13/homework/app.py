# -*- coding: utf-8 -*-

# Задача: добавить в блог возможность добавления комментариев.
# Их нужно добавлять использую ассинхронные запросы и `jQuery.ajax()`.
# Для тех, кому хочется еще задач:
# Добавить возможность ассинхронной загрузки комментариев
# Отрефакторить ваши шаблоны, сделать поддержку HTML 5 Boilerplate
# Нашему блогу осталось совсем чуть-чуть до завершения!


# import flask

from flask.ext.login import LoginManager

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_menu import Menu

import config


db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(user_id)

def create_app():
    from views import *

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config)

    # add menu
    Menu(app=app)

    # Blueprints:x`
    app.register_blueprint(blog)
    app.register_blueprint(login)
    app.register_blueprint(main_page)
    app.register_blueprint(bower_blueprint)

    db = SQLAlchemy(app)
    db.create_all()

    login_manager.init_app(app)
    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
