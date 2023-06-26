import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Lesson_19.libs.api.api import Api
from Lesson_19.libs.db.db import DB


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, timeout=10)
        self.api = Api()
        self.db = DB()

    def find(self, locator):
        logging.info(f'Click {locator}')
        return self.driver.find_element(locator)

    def wait_for(self, locator):
        logging.info(f'Wait until {locator} presence')
        return self._wait.until(EC.presence_of_element_located(locator))

    def check_title_on_page(self, title):
        self._wait.until(EC.title_is(title))

    def get_connection(self):
        self.db.connection()
