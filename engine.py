import json

engine_string = '{"lat": "43.9509", "lng": [34.4618]}'

# Getting dictionary
engine_dict = json.loads(engine_string)

# Pretty Printing JSON string back
print(json.dumps(engine_dict, indent = 4, sort_keys=True))