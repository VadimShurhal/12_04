import yaml
from pprint import pprint

#
# with open('test.yaml') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     pprint(data)


# with open('test.yaml') as f:
#     data = yaml.load_all(f, Loader=yaml.FullLoader)
#     pprint(data)
#
#
#
#     for _ in data:
#         for k, v in _.items():
#             print(f'{k} --- > {v}')



users = [{'name': 'Joe'},
         {'name':'Jack'}]


yaml_obj = yaml.dump(users)

print(yaml_obj)

print(type(yaml_obj))


#  .yaml  .yml

with open('my_yaml.yaml', 'w') as f:
    data = yaml.dump(users, f)



