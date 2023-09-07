import random

from locust import task, between, HttpUser, tag
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

    @task
    @tag('post')
    def get_all_posts(self):
        self.client.get('posts')

    @task
    @tag('crud')
    def crud(self):
        fake = Faker()

        user_id = random.randint(1, 5)
        post = {'userId': user_id,
                'title': fake.name(),
                'body': fake.sentence()}

        with self.client.post('posts', data=post, catch_response=True, name=f"Create user with id {user_id}") as response:
        # response = self.client.post('posts', data=post)
            print(f"Status code : {response.status_code}")
            if user_id == 3:
                raise SomeException("We can't create post")

            if user_id == 2:
                response.failure(f"We don't use user with id {user_id}")

        user_id = response.json().get('userId')

        # Get post for user
        self.client.get(f'posts/{user_id}')

        # Delete user
        self.client.delete(f'posts/{user_id}')
