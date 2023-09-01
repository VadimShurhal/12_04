import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:


    DROP_DOWN_XPATH = "//button[@class='site-nav-link'][contains(text(), '{}')]"

    DROP_DOWN_LIST = (By.CLASS_NAME, "site-nav-dropdown")
    ELEMENT_IN_DROPDOWN = "//a[@class='site-nav-dropdown_link'][contains(text(), '{}')]"

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, timeout=10)

    def find(self, locator):
        logging.info(f'Find element with locator {locator}')
        return self.driver.find_element(locator)

    def wait_for(self, locator):
        logging.info(f'Wait until {locator} presence')
        return self._wait.until(EC.presence_of_element_located(locator))

    def check_title_on_page(self, title):
        self._wait.until(EC.title_is(title))

    def click_element_in_dropdown(self, dropdown_name, element):
        try:
            self.find((By.XPATH, self.DROP_DOWN_XPATH.format(dropdown_name))).click()
            self.wait_for(self.DROP_DOWN_LIST)
            self.find((By.XPATH, self.ELEMENT_IN_DROPDOWN.format(element))).click()
        except:
            'Element not found'
