from abc import ABC, abstractmethod
from dataclasses import dataclass

#
# @dataclass
# class Position:
#     x: int = 0
#     y: int = 0
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
# class Character(ABC):
#     """Суперклас персонажів."""
#
#     def __init__(self, name: str):
#         self.name = name
#         self.position = Position()
#
#     @abstractmethod
#     def move(self, destination: Position):
#         print(f"{self.name} рухається з {self.position} на {destination}")
#         self.position = destination
#
#
# class Human(Character):
#     """Дочірній клас, який дотримується логіки батька."""
#
#     def move(self, destination: Position):
#         print(f"{self.name} йде з {self.position} на {destination}")
#         self.position = destination
#
#     def buy(self):
#         """Додає свою логіку."""
#         print("Купити предмет.")
#
#     def dead(self):
#         print("I'm dead, I was human")
#
#
# class Dragon(Character):
#     """Дочірній клас, який дотримується логіки батька."""
#
#     def move(self, destination: Position):
#         print(f"{self.name} летить з {self.position} на {destination}")
#         self.position = destination
#
#     def attack(self):
#         """Додає свою логіку."""
#         print("Викидати полум'я на супротивника.")
#
#     def dead(self):
#         print("I'm dead, I was dragon")
#
# def move(character: Character, destination: Position):
#     """
#     Клієнт, який використовує `Character` та його нащадків,
#      не помічаючи різниці.
#     """
#     character.move(destination)
#
# def dead(character: Character):
#     character.dead()
#
#
# spirit = Character("Spirit")
# john = Human("John")
# drogon = Dragon("Drogon")
#
# meeting_point = Position(x=300, y=250)
#
# move(spirit, meeting_point)
# move(john, meeting_point)
# move(drogon, meeting_point)
#
# dead(john)
# dead(drogon)

#before
# class Animal:
#
#     def __init__(self, attrs):
#         self.attribute = attrs
#
#     def eat(self):
#         print('Ate some food')
#
#
# class Cat(Animal):
#
#     def eat(self, amount=0.1):
#         if amount > 0.3:
#             print("Can't eat that match")
#         else:
#             print('Ate cat food')
#
#
# class Dog(Animal):
#
#     def eat(self):
#         print('Ate dog food')
#
#
# jack = Dog({'name': 'Jack', 'age': 2})
# abby = Dog({'name': 'Abby', 'age': 3})
#
# python = Cat(('Python', 3))
#
# animals = (jack, abby, python)
#
# for animal in animals:
#     if animal.attribute['age'] > 2:
#         print(animal.attribute['name'])

#after

class Animal:

    def __init__(self, name, age):
        self.attribute = {'name': name, 'age': age}

    def eat(self, _amount=0):
        print('Ate some food')


class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, amount=0.1):
        if amount > 0.3:
            print("Can't eat that match")
        else:
            print('Ate cat food')


class Dog(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self, _amount=0):
        print('Ate dog food')


jack = Dog('Jack', 2)
abby = Dog('Abby', 3)
python = Cat('Python', 3)

animals = (jack, abby, python)
print(animals)
for animal in animals:
    if animal.attribute['age'] > 2:
        print(animal.attribute['name'])


def eat(animal: Animal):
    animal.eat()

eat(jack)
eat(python)