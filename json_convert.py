import json

data_text = '{"p1": { "name": "A", "age": 20 }, "p2": { "name": "B", "age": 22 }}'
data = {"p1": {"name": "A", "age": 20}, "p2": {"name": "B", "age": 22}}

# json text -> dict
json.loads(data_text)

# dict -> json text
json.dumps(data)

# json file -> dict
with open('sample.json') as f:
    json.load(f)

# dict -> json file
with open('sample.json', 'w') as f:
    json.dump(data, f)
