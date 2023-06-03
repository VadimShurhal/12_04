import pytest

from Lesson_15.tests.example_user import Human


class TestSimple:

    def setup_class(self):
        self.human = Human('Joe', 18, 'pyhon')

    @pytest.mark.parametrize("language, expected_language", [('C++', 'C++'),
                                                             ('Kotlin', 'Kotlin'),
                                                             ('Java', 'Java'),
                                                             ('PHP', 'PHP')
                                                             ])
    def test_language_human(self, language, expected_language):
        self.human.change_language(language)
        assert self.human.language == expected_language

    @pytest.mark.parametrize("arg_1", [1, 2, 3])
    @pytest.mark.parametrize("arg_2", [3, 4, 5])
    def test_params(self, arg_1, arg_2):
        print(f'We gat arg_1 : {arg_1} and arg_2 {arg_2}')
        assert True


# 1-3 2-3 3-3 -> 2-3 3-3 3-4 ...