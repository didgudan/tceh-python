# -*- coding: utf-8 -*-

from datetime import date

from flask import Flask, request
from flask.ext.wtf import Form
from wtforms import validators, fields

import psycopg2

__author__ = 'sobolevn'

try:
    conn = psycopg2.connect(
        user='tceh',
        password='123',
        database='tceh_db',
        host='localhost',
        port=5432,
    )
except Exception as ex:
    print('I am unable to connect to the database', ex)

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'SECRET_KEY': 'very-secret',
    'WTF_CSRF_ENABLED': False,
})


class ObservationForm(Form):
    observation_date = fields.DateField(default=date.today())
    people_available = fields.IntegerField(
        validators=[validators.NumberRange(min=0)])


@app.route('/', methods=['GET', 'POST'])
def index():
    cur = conn.cursor()

    if request.method == 'POST':
        form = ObservationForm(request.form)
        if form.validate():
            od, pa = form.observation_date.data, form.people_available.data
            # YOU SHOULD NEVER DO THIS!
            # cur.execute(
            #     "INSERT INTO public.observations(people_available) "
            #     "VALUES ('%s');" % pa  # NEVER
            # )

            # do this instead:
            cur.execute(
                """INSERT INTO public.observations(
                    observation_date, people_available) VALUES (
                    %(od)s, %(pa)s)""",
                {'od': od.strftime('%Y-%m-%d'), 'pa': pa}
            )
            # conn.commit()  # why do we need this line?
            return str('posted')
        else:
            return str(form.errors)
    else:
        cur.execute(
            """SELECT * from public.observations;"""
        )
        data = cur.fetchall()  # note, that we are fetching the data here.
        return str(data)


if __name__ == '__main__':
    app.run(debug=True)
