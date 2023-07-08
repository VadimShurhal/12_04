import time

import allure

from Lesson_19.pages.home_page import HomePage
from Lesson_19.pages.login_page import LoginPage
from Lesson_19.pages.user_page import UserPage

USER_NAME = 'karpovolegggg@gmail.com'
USER_PASSWORD = 'Hillel2023!'


@allure.story('Create repository on GitHub')
class TestSelenium:

    @allure.description(f'Create repo for user {USER_NAME} with password {USER_PASSWORD}')
    @allure.title('Create repo')
    def test_selenium_2(self):
        home_page = HomePage(self.driver)
        home_page.check_title()
        home_page.click_login_button()
        time.sleep(5)
        login_page = LoginPage(self.driver)
        login_page.set_login(USER_NAME)
        login_page.set_password(USER_PASSWORD)
        login_page.click_sign_in_button()
        time.sleep(5)
        user_page = UserPage(self.driver)
        user_page.check_title()
        user_page.click_create_repo_button()

    @allure.description(f'Create repo for user {USER_NAME} with password {USER_PASSWORD}')
    @allure.title('Create repo')
    def test_selenium_3(self):
        home_page = HomePage(self.driver)
        home_page.check_title()
        home_page.click_login_button()
        time.sleep(5)
        login_page = LoginPage(self.driver)
        login_page.set_login(USER_NAME)
        login_page.set_password(USER_PASSWORD)
        login_page.click_sign_in_button()
        time.sleep(5)
        user_page = UserPage(self.driver)
        user_page.check_title()
        user_page.click_create_repo_button()

