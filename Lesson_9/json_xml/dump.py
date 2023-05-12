import datetime
import json

person = {
    "firstName": "John",
    "dateOfBirth": datetime.date(1969, 12, 31),
    "married": False,
    "spouse": None,
    "children": ["Bobby", "Molly"],
}


person_dumps = json.dumps(person, indent=4, default=str)
print(person_dumps)
print(type(person_dumps))

#
dict1 = {
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}

# the json file where the output must be stored
with open("myfile.json", "w") as file:
    json.dump(dict1, file, indent=6)










