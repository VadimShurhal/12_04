from pprint import pprint

import requests

# result = requests.get(' https://www.google.com')
# print(result)


URL = 'https://reqres.in/'

DATA = {
    "name": "Python",
    "job": "leader"
}

CHANGE_DATA = {
    "name": "Python",
    "job": "QA"
}

params_for_get = {'text': 'Samsung'}

header = {}
cookie = {}

# get_result = requests.get(URL + 'api/users?page=2')
# print(get_result.status_code)
# print(get_result)
#
# pprint(get_result.json())
#
#
# post_result = requests.post(URL + 'api/users', data=DATA)
# print(post_result.status_code)
# print(post_result)
# user_id = post_result.json().get('id')
# print(f'User id - {user_id}')
# pprint(post_result.json())
#
#
# post_result = requests.put(URL + 'api/users/2', data=CHANGE_DATA)
# print(post_result.status_code)
# print(post_result)
#
# pprint(post_result.json())
#
# delete_result = requests.delete(URL + f'api/users/2')
# print(get_result.status_code)
# print(get_result)
#
# pprint(get_result.json())

# get_result = requests.get('https://rozetka.com.ua/search/', params=params_for_get,
#                           headers=header,
#                           cookies=cookie)
# print(get_result.status_code)
# print(get_result)
#
# pprint(get_result.json())

STARWARS_API_URL = 'https://swapi.dev/api/'

result = requests.get(STARWARS_API_URL + 'people/1')
pprint(result.json())