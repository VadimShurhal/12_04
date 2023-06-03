from Lesson_15.tests.example_user import Human


class TestSimple:

    # def setup_class(self):
    #     self.human = Human('Joe', 18, 'pyhon')
    #     print(' Setup class ######################################################\n ')
    #
    # def teardown_class(self):
    #     print('\nteardown class ######################################################\n')

    # def setup(self):
    #     print('\nCreate human\n')
    #     self.human = Human('Joe', 18, 'pyhon')
    #
    # def teardown(self):
    #     print('\nMethod teardown\n')

    # def test_1(self):
    #     assert self.human.name == 'Joe'
    #
    # def test_2(self):
    #     self.human.grow()
    #     assert self.human.age == 19
    #
    # def test_3(self):
    #     self.human.change_language('Java')
    #     assert self.human.language == 'Java'
    #
    # def test_4(self):
    #     self.human.grow()
    #     assert self.human.age == 20

    def test_human_fixture(self, human):
        human.grow()
        assert human.age == 23


    def test_db_fixture(self, db):
        assert db.get('name') == 'Marta'

