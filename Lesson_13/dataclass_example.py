from dataclasses import dataclass


# class People:
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#
# @dataclass
# class People_d:
#     name: str
#     age: int
#
#
# people_1 = People('Joe', 22)
# people_2 = People_d('Marta', 33)
#
# print(people_1)
# print(people_2)
#
#
# people_1.name = "Mark"
# people_2.name = "Ann"
#
# print(people_1.name)
# print(people_2.name)


@dataclass(frozen=True)
class Student:
    name: str = 'Joe'
    age: int = 22


@dataclass
class Teacher:
    name: str
    students: list[Student]


student_1 = Student()
student_2 = Student('Marta', 23)
teacher = Teacher('Bob', [student_1, student_2])

print(teacher)
