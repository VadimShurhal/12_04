import allure
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Check title on login page')
    def check_title(self):
        assert self.driver.title == 'Sign in to GitHub · GitHub'

    @allure.step('Set login')
    def set_login(self, login):
        self.driver.find_element(By.ID, "login_field").send_keys(login)

    @allure.step('Set password')
    def set_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    @allure.step('Click sign button')
    def click_sign_in_button(self):
        self.driver.find_element(By.NAME, "commit").click()