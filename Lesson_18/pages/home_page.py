import allure
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Check title on home page')
    def check_title(self):
        assert self.driver.title == 'GitHub: Let’s build from here · GitHub'

    @allure.step('Click login button')
    def click_login_button(self):
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
