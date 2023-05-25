import enum
from http import HTTPStatus
import requests


# status_code = {'ok': 200,
#               'not_found': 404}
#
#
# r = requests.get('https:/www.google.com')
#
# if r.status_code == status_code.get('ok')

header_example = '''curl -i -H "Accept:application/json" -H "Content-Type:application/json"
 -H "Authorization: Bearer 92957b3161a1825213d52bb95f0f7a2e07e37f1d640242818d4b3fcb56faba21"
  -XPOST "https://gorest.co.in/public/v2/users" -d '{"name":"Tenali Ramakrishna", "gender":"male",
   "email":"tenali.ramakrishna@15ce.com", "status":"active"}'''

# class ApiSimple:
#
#     def get_token(self):
#         pass
#
#     @property
#     def get_header(self):
#         return  {'Accept':'application/json',
#                   "Content-Type":"application/json",
#                   "Authorization": f"Bearer {self.get_token()}"
#         }


# class StatusCode(int, enum.Enum):
#     OK = 200
#     NOT_FOUND = 404
#     SUCCESSFUL = 201


URL = 'https://gorest.co.in/public/v2'

class EndPoints(str, enum.Enum):
    POSTS = '/posts'
    COMMENTS = '/comments'
    TODOS = '/todos'
    PHOTO = '/photo'
#
# print(StatusCode.OK.value)
# print(StatusCode.OK.name)


# some_string = 'https://gorest.co.in/public/v2/posts'
#
# #
r = requests.get(URL + EndPoints.POSTS)
#
# if r.status_code == StatusCode.OK:
#     print(r.json())
#     print('Status code is OK')
#
#
# for _ in EndPoints:
#     print(_.name)
#     print(_.value)


class UserDict(dict, enum.Enum):
    student = {'name': 'Joe', 'age': 22}
    teacher = {'name': 'Marta', 'age': 44}


class StatusCode(enum.Enum):

    def __init__(self, status_code, description):
        self.status_code = status_code
        self.description = description

    OK = (200, 'Status OK')
    NOT_FOUND = (404, 'Status NOT_FOUND')
    SUCCESSFUL = (201, 'Status SUCCESSFUL')

print(StatusCode.OK.status_code)

