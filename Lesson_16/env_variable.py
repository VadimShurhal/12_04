import os


print(os.environ.items())

os.environ['API_KEY'] = 'hhwda213-432-dwa231'
new_variable = os.getenv('API_KEY')


print(new_variable)


print(os.getenv('ENV'))
print(os.getenv('browser'))