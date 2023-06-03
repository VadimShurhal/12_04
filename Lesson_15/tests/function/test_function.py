# def setup_module():
#     print(' Setup modul ######################################################\n ')
#
#
# def teardown_module():
#     print('\nteardown module ######################################################\n')
#
#
# def setup_function():
#     print('\nfunction setup\n')
#
#
# def teardown_function():



def test_human_name(human):
    assert human.name == 'Joe'


def test_human_grow(human):
    human.grow()
    assert human.age == 56


def test_human_language(human):
    human.change_language('Java')
    assert human.language == 'Java'
