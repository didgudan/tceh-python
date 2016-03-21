class Storage(object):
    obj = None

    blog_posts = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.api_posts = []
        return cls.obj
