from locust import User, task, constant, between


class MyFirstTest(User):

    # wait_time = constant(2)
    wait_time = between(2, 7)

    def on_start(self):
        # get user data (first name, password)
        # try get token
        # login
        print('We start our test')

    @task
    def first(self):
        print("My first test")
        print('--------------------------')

    @task
    def second(self):
        print("Second test")
        print('--------------------------')

    def on_stop(self):
        # logout
        print('We finished our test')
