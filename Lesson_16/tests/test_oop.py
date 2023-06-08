import logging

import pytest


class TestSimple:

    @pytest.mark.fast
    @pytest.mark.regression
    def test_human_fixture(self, human):
        human.grow()
        logging.info('test_human_fixture')
        assert human.age == 23

    def test_db_fixture_name(self, db):
        logging.info('test_human_fixture')
        assert db.get('name') == 'Marta'

    @pytest.mark.regression
    def test_db_fixture_age(self, db):
        logging.info('test_human_fixture')
        assert db.get('age') == 15

    @pytest.mark.fast
    def test_db_fixture_fail(self, db):
        logging.debug('test_human_fixture')
        assert db.get('name') != 'Mark'

    @pytest.mark.regression
    def test_db_fixture_age_2(self, db):
        logging.info('test_db_fixture_age_2')
        assert db.get('age') == 15

    @pytest.mark.regression
    def test_db_fixture_age_3(self, db):
        logging.debug('test_db_fixture_age_3')
        assert db.get('age') == 15

    @pytest.mark.regression
    def test_human_fixture_action(self, human):
        assert human.action.name == 'jumping'