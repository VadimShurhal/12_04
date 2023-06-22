import allure
from selenium.webdriver.common.by import By

from Lesson_19.constants import GithubTitles
from Lesson_19.pages.base_page import BasePage
from Lesson_19.pages.user_page import UserPage


class LoginPage(BasePage):

    LOGIN_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, "commit")

    @allure.step('Check title on login page')
    def check_title(self):
        self.check_title_on_page(GithubTitles.LOGIN_PAGE_TITLE)
        return self

    @allure.step('Set login')
    def set_login(self, login):
        self.wait_for(self.LOGIN_FIELD).send_keys(login)
        return self

    @allure.step('Set password')
    def set_password(self, password):
        self.wait_for(self.PASSWORD_FIELD).send_keys(password)
        return self

    @allure.step('Click sign button')
    def click_sign_in_button(self):
        self.wait_for(self.SIGN_IN_BUTTON).click()
        return UserPage(self.driver)
