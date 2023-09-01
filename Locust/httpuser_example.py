import random

from locust import task, between, HttpUser
from faker import Faker


class TestLoadUser:

    def test_load_users(self):
        # DB query
        # API load
        ...


class SomeException(Exception):
    pass


class MyFirstTest(HttpUser):

    wait_time = between(2, 3)

    def on_start(self):
        load = TestLoadUser()
        load.test_load_users()

    @task(6)
    def get_all_posts(self):
        self.client.get('posts')

    @task(2)
    def crud(self):
        fake = Faker()

        user_id = random.randint(1, 5)
        post = {'userId': user_id,
                'title': fake.name(),
                'body': fake.sentence()}

        responce = self.client.post('posts', data=post)
        if user_id < 10:
            raise SomeException("We can't create post")

        user_id = responce.json().get('userId')

        # Get post for user
        self.client.get(f'posts/{user_id}')

        # Delete user
        self.client.delete(f'posts/{user_id}')
