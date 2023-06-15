import allure
from selenium.webdriver.common.by import By


class CreateRepoPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Check title on repo page')
    def check_title(self):
        assert self.driver.title == 'New repository · GitHub'

    @allure.step('Set repo name')
    def set_repo_name(self, repo_name):
        self.driver.find_element(By.ID, "react-aria-2").send_keys(repo_name)

    @allure.step('Set repo description')
    def set_repo_description(self, description):
        self.driver.find_element(By.ID, "react-aria-3").send_keys(description)

    @allure.step('Click readme file')
    def click_add_readme_file(self):
        self.driver.find_element(By.ID, "react-aria-8").click()

    @allure.step('Click create repo button')
    def click_create_repo_button(self):
        self.driver.find_element(By.XPATH, "//button//span[contains(text(), 'Create repository')]").click()

