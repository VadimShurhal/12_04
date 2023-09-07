from locust import task, TaskSet, HttpUser, constant


class PostSet(TaskSet):

    @task
    def get_all_posts(self):
        self.client.get('posts')
        print('Get posts')


class CommentsSet(TaskSet):

    @task
    def get_all_comments(self):
        self.client.get('comments')
        print('Get comments')


class TodoSet(TaskSet):

    @task
    def get_all_to_do(self):
        self.client.get('todos')
        print('Get todos')


class LoadTest(HttpUser):
    host = "https://jsonplaceholder.typicode.com/"
    tasks = [PostSet, CommentsSet, TodoSet]
    wait_time = constant(1)
