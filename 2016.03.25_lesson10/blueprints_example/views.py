# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, jsonify

__author__ = 'sobolevn'


views = Blueprint('views', __name__, url_prefix='/views')
admin = Blueprint('admin', __name__, url_prefix='/admin')
# https://github.com/apiguy/flask-classy


# Views:

@views.route('/')
@views.route('/index', strict_slashes=False)
@views.route('/index/<int:index_id>')
def index_by_id(index_id=0):
    return 'some response ' + str(index_id)


@views.route('/index/<string:index_title>')
def index_by_title(index_title):
    return 'title ' + index_title


@views.route('/<path:path>')
def catch_all(path):
    return 'you path was ' + path


# Admin pages:

@admin.route('/')
def admin_view():
    urls = {
        'local': url_for('.admin_view'),
        'full_external': url_for('views.index_by_id'),
        'full_local': url_for('admin.admin_view'),
    }
    return jsonify(urls)
