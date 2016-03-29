# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_babel import Babel

__author__ = 'sobolevn'


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def locale_select():
    return request.accept_languages.best_match()
