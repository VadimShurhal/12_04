import pytest

from Lesson_15.tests.example_user import Human


# function
# cls
# modulefinder
# session

@pytest.fixture(scope='session')
def human():
     Human('Joe', 22, 'Python')


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
def browser():
    print("\nbrowser open\n")
    driver = browser.open()
    # setup
    yield driver
    # teardown
    print("\nbrowser closed\n")
    driver.close()