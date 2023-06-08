import os

import pytest


# skipif, skip, xfail
# @pytest.mark.skipif(os.getenv('browser') != 'chrome', reason="browser not support")
class TestSimple2:

    # @pytest.mark.skipif(reason='Bug 123')
    def test_human_fixture(self, human):
        human.grow()
        print('test_human_fixture')
        if human.age != 50:
            pytest.xfail("Age not equal 50")

    # @pytest.mark.skip()
    def test_db_fixture_name(self, db):
        print('test_human_fixture')
        assert db.get('name') == 'Marta'

    @pytest.mark.xfail(os.getenv('browser') != 'firefox', reason="browser not support")
    def test_db_fixture_age(self, db):
        print('test_human_fixture')
        assert db.get('age') == 22
