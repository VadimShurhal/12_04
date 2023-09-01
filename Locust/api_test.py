import faker
import requests
from faker import Faker

fake = Faker()

r = requests.get("https://jsonplaceholder.typicode.com/posts/")
print(r)

post = {'userIds': 12,
        'title': fake.name(),
        # 'body': fake.sentence()
        }


r = requests.post("https://jsonplaceholder.typicode.com/users/1/posts", data=post)
post_id = r.json().get('userId')


r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
print(r)


r = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
print(r)