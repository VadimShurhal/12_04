class Human:

    def __init__(self, name: str, age: int, language: str):
        self.name = name
        self.age = age
        self.language = language

    def change_language(self, new_language):
        self.language = new_language

    def grow(self):
        self.age += 1