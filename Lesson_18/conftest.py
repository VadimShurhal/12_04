import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Lesson_18.pages.create_repo_page import CreateRepoPage
from Lesson_18.pages.home_page import HomePage
from Lesson_18.pages.login_page import LoginPage
from Lesson_18.pages.user_page import UserPage


def pytest_exception_interact(node):
    driver = node.instance.driver
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    request.cls.driver = driver
    request.cls.home_page = HomePage(driver)
    request.cls.login_page = LoginPage(driver)
    request.cls.user_page = UserPage(driver)
    request.cls.create_repo_page = CreateRepoPage(driver)
    driver.get("https://github.com/")
    driver.maximize_window()
    yield
    driver.quit()
