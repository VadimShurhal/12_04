class ToDoList:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     with open(filename, 'w') as f:
    #         f.write(str(self))
    #
    # def send_to_server(self):
    #     pass


t = ToDoList()
t.add_entry('Clean the kitchen')
t.add_entry('Do homework')
print(t)

file_name = 'text.txt'
# t.save(file_name)


class SaveManager:

    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))


SaveManager.save_to_file(t, file_name)