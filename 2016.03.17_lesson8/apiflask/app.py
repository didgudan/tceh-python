# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

import config
from storage import Storage
from models import APIModel
from forms import APIForm


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def new_post():
    storage = Storage()
    post_result = None

    if request.method == 'POST':
        form = APIForm(request.form)
        if form.validate():
            post_result = "Posted successful"
            storage.api_posts.append(APIForm(form.data))
    else:
        form = APIForm()

    return render_template(
         'home.html',
        form=form,
        post_result=post_result,
    )

if __name__ == '__main__':
    app.run()
