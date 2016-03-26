import json
import jsonschema
import os
import jsonref

with open("parent.json") as f:
    parent = jsonref.load(f)

with open("data.json") as f:
    json_data = json.load(f)

# try:
jsonschema.validate(json_data, parent)
# except jsonschema.ValidationError as e:
#     print(e)
# except jsonschema.SchemaError as e:
#     print(e)
