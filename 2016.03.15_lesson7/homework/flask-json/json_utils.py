import os.path
from flask import json

from models import BlogPostModel


json_backend = "blog.json"


def initialize_json():
    if not os.path.isfile(json_backend):
        with open(json_backend, "w") as f:
            json.dump([], f)

def load_objects_from_json():
  with open(json_backend) as f:
    data = json.load(f)

    objects = []
    for object_ in data:
        objects.append(BlogPostModel(object_))

    return objects

def make_dicts_from_object_list(object_list):
    dict_ = []
    for elem in object_list:
        dict_.append(elem.__dict__)

    return dict_

def save_to_json(_object):
    objects_from_json = load_objects_from_json()
    objects_from_json.append(_object)
    dicts_from_json = make_dicts_from_object_list(objects_from_json)

    with open(json_backend, "w") as f:
        json.dump(dicts_from_json, f)