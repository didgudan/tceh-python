# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form

import config

import json

__author__ = 'sobolevn'


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from models import User, Post

    post_form_class = model_form(Post, base_class=Form, db_session=db.session)

    if request.method == 'POST':
        # For full example:
        # http://flask.pocoo.org/snippets/60/

        # alternative:
        # https://wtforms-alchemy.readthedocs.org/en/latest/introduction.html
        user = User.query.filter_by(username='sobolevn').first()
        print("{} is creating a new {}'th post!".format(
            user.username, len(user.posts.all()) + 1))

        form = post_form_class(request.form)
        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')

    else:
        form = post_form_class()

    posts = Post.query.filter_by(is_visible=True).all()
    return render_template('home.html', form=form, posts=posts)


if __name__ == '__main__':
    from models import *
    db.create_all()

    app.run()
