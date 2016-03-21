# -*- coding: utf-8 -*-


from flask import Flask, request, render_template, json

import config
from models import BlogPostModel
from forms import BlogPostForm
from json_utils import initialize_json, load_objects_from_json, save_to_json

# Дорабатывает блог.
# Задача: сохранять записи при выходе из приложения в json-файл, загружать
# записи из json-файла при старте flask.
#
# Задание со звездочкой (сложное): генируем для каждого поста QR-код и выдаем
# пользователю


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)



@app.route('/', methods=['GET'])
def home():
    initialize_json()

    return render_template(
        'home.html',
        blog_posts=load_objects_from_json()
    )


@app.route('/post', methods=['GET', 'POST'])
def new_post():
    initialize_json()
    post_result = None

    if request.method == 'POST':
        form = BlogPostForm(request.form)
        if form.validate():
            new_post = BlogPostModel(form.data)
            save_to_json(new_post)
            post_result = "Posted successful"
    else:
        form = BlogPostForm()

    return render_template(
        'new_post.html',
        form=form,
        post_result=post_result,
    )


if __name__ == '__main__':
    app.run()
