import datetime


class BlogPostModel(object):
    def __init__(self, form_data):
        self.author = form_data['author']
        self.title = form_data['title']
        self.text = form_data['text']
        self.date = datetime.datetime.now().strftime("%H:%M %d.%m.%Y")
        self.base64_qr_code = ""
