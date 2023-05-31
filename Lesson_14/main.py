from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Human:
    name: str
    age: int


human = Human('Joe', 15)

print(human.age)
print(human.age)
print(type(human))


#to dict
human_dict = human.to_dict()
print(type(human_dict))
print(human_dict)

#to_json
human_json = human.to_json()
print(type(human_json))
print(human_json)


user = {'name': 'Marta',
        'age': 22}

user_2 = '{"name": "Tom", "age": 33}'

new_user = Human.from_dict(user)
print(new_user)
print(type(new_user))
print(new_user.age)
print(new_user.name)
new_user.age = 44
print(new_user.age)

new_user_2 = Human.from_json(user_2)
print(new_user_2)
print(type(new_user_2))