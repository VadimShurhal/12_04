import pytest


class TestClass:

    def setup(self):
        print('Setup method')

    def teardown(self):
        print('teardown method')

    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    def test_isupper(self):
        assert 'FOO'.isupper()

    def test_failed_upper(self):
        assert 'foo'.upper() == 'FOo'
