# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
    request,
    redirect,
    render_template,
    flash,
    url_for,
)
from flask.ext.login import (
    login_required,
    login_user,
    logout_user,
    current_user,
)

from models import User
from app import db
from forms import RegisterForm, LoginForm

__author__ = 'sobolevn'


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', form=RegisterForm())

    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('User successfully registered')
        return redirect(url_for('.login'))
    else:
        flash('Incorrect registration!')
        return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', form=LoginForm())

    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = form.user
        login_user(user, remember=True)
        return 'Login successful. Current user: {}'.format(
                current_user.username)
    else:
        flash('Incorrect attempt!')
        return render_template('login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return 'You are now logge'


@auth.route('/profile')
@login_required
def view():
    return 'Only logged-in user can see me! Current: {}'.format(
            current_user.username)
