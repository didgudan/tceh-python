# -*- coding: utf-8 -*-

from flask import Flask
from views import views, admin

__author__ = 'sobolevn'

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'DEFAULT_RESPONSE': 'hello, world!',
})

# Do some extra init:
app.register_blueprint(views)
app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()
