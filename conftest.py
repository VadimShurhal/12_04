import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://github.com/", help="my option: type1 or type2"
    )

# @pytest.fixture
# def url(request):
#     return request.config.getoption("--url")

#
# def pytest_exception_interact(node):
#     driver = node.instance.driver
#     allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    request.cls.driver = driver
    url = request.config.getoption("--url")
    # url = os.getenv('URL')
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()

# @pytest.fixture(autouse=True, scope='session')
# def driver(url):
#     # setup
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.implicitly_wait(5)
#     driver.get(url)
#     driver.maximize_window()
#     #return object driver
#     yield driver
#     # teardown
#     driver.quit()


# @pytest.fixture(autouse=True, scope='session')
# def driver():
#     db = db()
#     db.connection()
#     yield db
#     bd.close()


