import logging

import pytest


def devision(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        print(f'Sum {a} and {b} {a+b}')


def test_zero_devision():
    print('Some text')
    with pytest.raises(ZeroDivisionError):
        devision(1, 0)


class NotValidUrlException(BaseException):
    pass


def check_url(url):
    # try:
    #     print(url)
    # except NotValidUrlException:
    #     logging.info(f'Not valid url {url}')
    raise NotValidUrlException



UNVALID_URL_DATA = ['www.google.com', 'www.google.', 'https://www.google.', 'www.google.', 'https://www.google.']


@pytest.mark.parametrize("url", UNVALID_URL_DATA)
def test_check_unvalid_link(url):
    print('Some text')
    with pytest.raises(NotValidUrlException):
        check_url(url)



