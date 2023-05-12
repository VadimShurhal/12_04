import json

with open('example.json') as f:
    templates = json.load(f)

print(templates)
print(type(templates))


json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data = json.loads(json_string)
print(data)
print(type(data))
