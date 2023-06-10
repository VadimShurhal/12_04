import pytest




# function
# cls
# modulefinder
# session

@pytest.fixture(scope='session')
def db():
    print("\ndb open\n")
    db = {'name': "Marta",
          'age': 15}
    # setup
    yield db
    # teardown
    print("\ndb closed\n")


@pytest.fixture(scope='session')
def db2(request):
    print("\ndb open\n")

    def teardown():
        print("\ndb closed\n")

    request.addfinalizer(teardown)


# @pytest.fixture(scope='session')
# def generate_data():
#     login = "vadym@hillel.com"
#     password = 'khda78d9y32'
#     data = {'login' : login,
#             'password': password}
#     return data

@pytest.fixture(autouse=True)
def generate_data_with_request(request):
    request.cls.login = "vadym@hillel.com"
    request.cls.password = "khda78d9y32"
    print(request.fixturename)
    print(request.scope)
    print(request.module)
    print(request.instance)
    print(request.path)
    print(request.session)
    print(request.function)





