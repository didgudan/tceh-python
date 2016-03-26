# -*- coding: utf-8 -*-

import os
from flask import Flask, request, render_template, json
from flask.json import JSONEncoder, JSONDecoder

import config
from models import BlogPostModel
from forms import BlogPostForm

# Дорабатывает блог.
# Задача: сохранять записи при выходе из приложения в json-файл, загружать
# записи из json-файла при старте flask.
#
# Задание со звездочкой (сложное): генируем для каждого поста QR-код и выдаем
# пользователю


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

json_backend = "blog.json"

class PostEncoder(JSONEncoder):
    def default(self, obj):
        return [obj.__dict__]



def make_empty_file():
    with open(json_backend, 'w') as f:
        json.dump('', f)


mdef from_json(json_object):
    
    if 'author' in json_object:
        return BlogPostModel(json_object)

def load_from_json():
    with open(json_backend, "r") as f:
        load_data = json.load(f)
        posts = JSONDecoder(object_hook = from_json).decode(load_data)

            return posts
    except IOError as err:
        make_empty_file()
        return []


def save_to_json(data):
    from_json = load_from_json()
    if len(from_json) < 2:
        from_json = data
    with open(json_backend, 'w') as f:
        json.dump(from_json, f, cls=PostEncoder)


@app.route('/', methods=['GET'])
def home():
    return render_template(
        'home.html',
        blog_posts=load_from_json()
    )


@app.route('/post', methods=['GET', 'POST'])
def new_post():
    post_result = None

    if request.method == 'POST':
        form = BlogPostForm(request.form)
        if form.validate():
            new_post = BlogPostModel(form.data)
            save_to_json(
                PostEncoder().encode(new_post)
            )
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
