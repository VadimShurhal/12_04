import os

import pycodestyle
# from pyflakes.scripts import pyflakes

# DIR = os.path.normpath('Lesson_1')

config_file = os.path.normpath('tox.ini')
paths_to_check = ['Lesson_1']


class TestCommitVerification:

    def test_pep8_conformance(self):
        style = pycodestyle.StyleGuide(config_file=config_file)
        report = style.check_files(paths=paths_to_check)
        assert report.get_count() == 0,  'Please check PEP 8 errors'

    # def test_unused_import_and_vars(self):
    #     count_of_unused = pyflakes.checkRecursive(paths_to_check, reporter=None)
    #     assert count_of_unused == 0, 'Please check pyflakes errors'

