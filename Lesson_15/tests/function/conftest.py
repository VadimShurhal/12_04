import pytest

from Lesson_15.tests.example_user import Human


@pytest.fixture()
def human():
    return Human('Joe', 55, 'Python')