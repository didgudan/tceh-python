# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, Blueprint

__author__ = 'sobolevn'

app = Flask(__name__)
app.config['DEBUG'] = True


base_dir = os.path.dirname(__file__)

# serving `bower` files:
bower_blueprint = Blueprint(
    'bower', __name__, static_url_path='/vendor',
    static_folder=os.path.join(base_dir, 'bower_components')
)
app.register_blueprint(bower_blueprint)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

