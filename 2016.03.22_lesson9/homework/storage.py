import json


class Storage(object):
    # obj = None
    #
    # blog_posts = None

    # @classmethod
    # def __new__(cls, *args):
    #     if cls.obj is None:
    #         cls.obj = object.__new__(cls)
    #         cls.blog_posts = []
    #     return cls.obj

    def __init__(self, app_config=None):
        self.blog_posts = []

        if app_config:
            self.backend = app_config['BACKEND']

    def __getattribute__(self, name):
        # if self.backend == "json":
        return super(Storage, self).__getattribute__(name)

    # don't working on storage.blog_posts.append(BlogPostModel(form.data))
    def __setattr__(self, name, val):
        super(Storage, self).__setattr__(name, val)
