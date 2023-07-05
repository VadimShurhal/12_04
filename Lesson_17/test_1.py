# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC


class Test1:

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def search_element(self, by, selector):
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])
        return wait.until(EC.element_to_be_clickable((by, selector)))

    def test_1(self):
        self.driver.get("https://www.selenium.dev/")
        self.driver.set_window_size(1093, 726)
        # self.driver.maximize_window()
        self.search_element(By.ID, "Layer_1").click()
        self.search_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) span").click()
        self.search_element(By.LINK_TEXT, "CHANGELOG").click()
        self.search_element(By.LINK_TEXT, "SeleniumHQ").click()
        self.search_element(By.CSS_SELECTOR, ".mb-3:nth-child(3) .repo").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.search_element(By.LINK_TEXT, ".github").click()

    def test_2(self):
        self.driver.get("https://www.selenium.dev/")
        assert self.driver.title == self.login