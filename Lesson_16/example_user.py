class Action:
    def __init__(self, name):
        self.name = name


class Human2:

    def __init__(self, name: str, age: int, language: str, action: Action):
        self.name = name
        self.age = age
        self.language = language
        self.action = action

    def change_language(self, new_language):
        self.language = new_language

    def grow(self):
        self.age += 1