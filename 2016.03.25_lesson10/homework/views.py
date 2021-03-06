# -*- coding: utf-8 -*-

from flask import (
    request,
    render_template,
    flash,
    redirect,
    Blueprint,
    url_for,
    abort,
)

from flask.ext.login import (
    login_required,
    login_user,
    logout_user,
    current_user,
)

import time

from wtforms.ext.sqlalchemy.orm import model_form
from flask.ext.wtf import Form
from forms import RegisterForm, LoginForm

from app import db
from models import *

blog = Blueprint('blog', __name__, url_prefix='/blog')
login = Blueprint('login', __name__, url_prefix='/login')
main_page = Blueprint('root', __name__, url_prefix='/')


@main_page.route("/", methods=['GET'])
def root():
    return redirect(url_for('blog.home'))

@blog.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        Post.query.filter_by(id=request.form['id']).first().is_visible = False
        db.session.commit()
        print("Set invisible mark to post with id %s" %request.form['id'])

    post_form_class = model_form(Post, base_class=Form, db_session=db.session)
    form = post_form_class()
    posts = Post.query.filter_by(is_visible=True).all()

    return render_template('home.html', form=form, posts=posts)


@blog.route('/post', methods=['GET', 'POST'])
@login_required
def new_post():
    post_form_class = model_form(Post, base_class=Form, db_session=db.session)

    if request.method == 'POST':
        user = User.query.filter_by(id=request.form['user']).first()
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

    return render_template('new_post.html', form=form)


@login.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'GET':
        return render_template('register.html', form=form)

    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('User successfully registered')
        return redirect(url_for('.login_page'))


@login.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', username=current_user.username)

@login.route('/logout', methods=['GET', 'POST'])
def logout_page():
    logout_user()
    flash('Successfully logged out!')
    return redirect(url_for('.login_page'))

@login.route('/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        registered_user = User.query.filter_by(
            username=request.form['username']).first()

        if (registered_user is None) or \
           (registered_user.check_password(request.form['password']) is False):
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('.login_page'))

        login_user(registered_user)

        # next = request.args.get('next')
        # # next_is_valid should check if the user has valid
        # # permission to access the `next` url
        # if not next_is_valid(next):
        #     return abort(400)

        return redirect(url_for('.profile'))
    return render_template('login.html', form=form)
