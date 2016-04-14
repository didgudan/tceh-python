# -*- coding: utf-8 -*-

# Задача: добавить в свой блог авторизацию.
# Пользователь должен перед отправкой сообщения зарегистрироваться и зайти в
# свой профиль. Неавторизованные пользователи не могут постить, только читать.
#
# Задачи со звездочкой:
#   При регистрации пользователю отправляется email, что он успешно
#       зарегистрирован
#   В блоге есть возможность выбрать язык меню


# import flask

from flask.ext.login import LoginManager

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
