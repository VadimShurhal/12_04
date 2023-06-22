import allure
from selenium.webdriver.common.by import By

from Lesson_19.constants import GithubTitles
from Lesson_19.pages.base_page import BasePage


class UserPage(BasePage):

    CREATE_REPO_BUTTON = (By.XPATH, "//h2/a")

    @allure.step('Check title on user page')
    def check_title(self):
        self.check_title_on_page(GithubTitles.USER_PAGE)
        return self

    @allure.step('Click create repo button')
    def click_create_repo_button(self):
        self.wait_for(self.CREATE_REPO_BUTTON).click()
