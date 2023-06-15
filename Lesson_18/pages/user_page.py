import allure
from selenium.webdriver.common.by import By


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Check title on user page')
    def check_title(self):
        assert self.driver.title == 'GitHub'

    @allure.step('Click create repo button')
    def click_create_repo_button(self):
        self.driver.find_element(By.XPATH, "//h2/a").click()
