from json import JSONEncoder, JSONDecoder

class FileItem:
    def __init__(self, params):
        self.fname = params['fname']
        # self.fname = params

# f  = FileItem({"fname": "/foo/bar"})
# f  = FileItem("/foo/bar")

# class MyEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__

# print(MyEncoder().encode(f))

def from_json(json_object):
    # for elem in json_object:
    if 'fname' in json_object:
        return FileItem(json_object)   

f_decoded = JSONDecoder(object_hook = from_json).decode('{"fname": "object_hook"}')
print(f_decoded)