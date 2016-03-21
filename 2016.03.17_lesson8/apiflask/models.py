import datetime


class APIModel(object):
    def __init__(self, form_data):
        self.name = form_data['name']
        self.email = form_data['email']
