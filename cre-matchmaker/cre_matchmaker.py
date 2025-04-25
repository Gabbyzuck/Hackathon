import json

with open('data/properties.json') as f:
    properties = json.load(f)

print(properties)