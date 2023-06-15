import os

import allure
import pytest


@allure.story('Test pytest params')
class TestAllure:

    @pytest.mark.parametrize("language, expected_language", [('C++', 'C++'),
                                                             ('Kotlin', 'Kotlin'),
                                                             ('Java', 'Java'),
                                                             ('PHP', 'PHP')
                                                             ])
    def test_language_human(self, language, expected_language):
        assert language == expected_language

    @pytest.mark.parametrize("arg_1", [1, 2, 3])
    @pytest.mark.parametrize("arg_2", [3, 4, 5])
    def test_params(self, arg_1, arg_2):
        print(f'We get arg_1 : {arg_1} and arg_2 {arg_2}')
        assert True

    @pytest.mark.skipif(True, reason='Bug 123')
    def test_human_fixture(self, human):
        print('test_human_fixture')

    @pytest.mark.skip()
    def test_db_fixture_name(self, db):
        print('test_human_fixture')

    @pytest.mark.xfail(os.getenv('browser') != 'firefox', reason="browser not support")
    def test_db_fixture_age(self, db):
        print('test_human_fixture')
