import json

class BlogPostModel(object):
    def __init__(self, form_data):
        self.author = form_data['author']

# post = BlogPostModel({"author": "me"})
# print("original post is %s" %post.__dict__)
# with open('test.json', "w") as f:
#     json.dump([post.__dict__], f)

def initialize_json():
    with open('test.json', "w") as f:
        json.dump([], f)        

initialize_json()

post1 = BlogPostModel({"author": "you"})
with open('test.json') as f:
    data = json.load(f)

    objects = []
    for object_ in data:
        objects.append(BlogPostModel(object_))
print("data from file is %s" %data)
print("objects are %s" %objects)

objects.append(post1)
print("appended data is %s" %objects)
