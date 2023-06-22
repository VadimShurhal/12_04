import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_exception_interact(node):
    driver = node.instance.driver
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    request.cls.driver = driver
    driver.get("https://github.com/")
    driver.maximize_window()
    yield
    driver.quit()
