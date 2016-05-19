import requests
import json
import time
import pdb

from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    current_context = {}

    if request.method == 'POST':
        start_time_main = time.time()
        r_index = requests.get("http://127.0.0.1:8000/api/v1/")
        r_lessons = requests.get("http://127.0.0.1:8000/api/v1/lesson/")
        r_themes = requests.get("http://127.0.0.1:8000/api/v1/theme/")
        api_request_time = time.time() - start_time_main

        if r_index.status_code == 200 and r_lessons.status_code == 200 \
                and r_themes.status_code == 200:

            _result = "Successfully connected to local API!"
            index_result = json.loads(r_index.content)
            lessons_result = json.loads(r_lessons.content)
            themes_result = json.loads(r_themes.content)

            current_context.update({
                'index_result': index_result,
                'lessons_result': lessons_result,
                'themes_result': themes_result,
            })
        else:
            _result = "Something went wrong with connection to local API"

        current_context.update({
            "connection_result": _result,
            'api_request_time': api_request_time,
        })


    c = RequestContext(request, current_context)

    return render_to_response('get_from_api/index.html', c)
