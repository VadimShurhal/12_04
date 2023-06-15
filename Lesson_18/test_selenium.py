import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

USER_NAME = 'karpovolegggg@gmail.com'
USER_PASSWORD = 'Hillel2023!'


@allure.story('Create repository on GitHub')
class TestTestselenium:

    @allure.description(f'Create repo for user {USER_NAME} with password {USER_PASSWORD}')
    @allure.title('Create repo')
    def test_selenium(self):
        self.home_page.check_title()
        self.home_page.click_login_button()

        self.login_page.check_title()
        self.login_page.set_login(USER_NAME)
        self.login_page.set_password(USER_PASSWORD)
        self.login_page.click_sign_in_button()

        self.user_page.check_title()
        self.user_page.click_create_repo_button()

        self.create_repo_page.check_title()
        self.create_repo_page.set_repo_name('Test_repo_4')
        self.create_repo_page.set_repo_description('Test description 4')
        self.create_repo_page.click_add_readme_file()
        time.sleep(4)
        self.create_repo_page.click_create_repo_button()

        time.sleep(4)
        with allure.step('Check repo name in current url'):
            assert 'Test_repo_4' in self.driver.current_url

