import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://github.com/", help="Base url")


def pytest_exception_interact(node):
    driver = node.instance.driver
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(autouse=True)
def driver(request):
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "114.0",
        "selenoid:options": {
            "enableVideo": False,
            "enableVNC": True,
            "enableLog": True
        }
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    request.cls.driver = driver
    url = request.config.getoption("--url")
    driver.get(url)
    driver.maximize_window()
    yield
    driver.quit()
