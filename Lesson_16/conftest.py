import pytest


# function
# cls
# modulefinder
# session
from Lesson_16.example_user import Action, Human2


@pytest.fixture(scope='session')
def action():
    return Action('jumping')


@pytest.fixture(scope='session')
def human(action):
    return Human2('Joe', 22, 'Python', action)


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
