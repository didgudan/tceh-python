# -*- coding: utf-8 -*-

# Задача: добавить поддержку базы данных для вашего блога. Для чего будем
# использовать библиотеку `SQLAlchemy`. Заменить старые формы на формы моделей,
# выбрать библиотеку можно самостоятельно.
# Подзадачи:
# 1) Добавить возмонжость сохранять посты в базе, используя новые формы.
#     В формах не должно быть лишних "технических" полей: даты, видимости
# и так далее.
# 2) Добавить возможность удалять люьой пост.
# 3) Показываться должны только посты, которые не удалены.
# Задача со звездочкой:
# Добавить возмжность регистрации, входа и выхода.


from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms.ext.sqlalchemy.orm import model_form
from flask.ext.wtf import Form
from flask_zurb_foundation import Foundation

import config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)
Foundation(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        Post.query.filter_by(id=request.form['id']).first().is_visible = False
        db.session.commit()
        print("Set invisible mark to post with id %s" %request.form['id'])

    post_form_class = model_form(Post, base_class=Form, db_session=db.session)
    form = post_form_class()
    posts = Post.query.filter_by(is_visible=True).all()

    return render_template('home.html', form=form, posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def new_post():
    post_form_class = model_form(Post, base_class=Form, db_session=db.session)

    if request.method == 'POST':
        # For full example:
        # http://flask.pocoo.org/snippets/60/

        # alternative:
        # https://wtforms-alchemy.readthedocs.org/en/latest/introduction.html
        user = User.query.filter_by(username='Alex').first()
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


if __name__ == '__main__':
    from models import *
    db.create_all()
    app.run()
