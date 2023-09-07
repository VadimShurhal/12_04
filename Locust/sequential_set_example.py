import time
from datetime import datetime
import random

from locust import task, TaskSet, HttpUser, constant, SequentialTaskSet, constant_pacing


class PostSet(SequentialTaskSet):

    @task
    def get_all_posts(self):
        sec = random.randint(1, 10)
        self.client.get('posts')
        time.sleep(sec)
        print(datetime.now())


class LoadTest(HttpUser):
    # host = "https://jsonplaceholder.typicode.com/"
    tasks = [PostSet]
    wait_time = constant_pacing(2)
