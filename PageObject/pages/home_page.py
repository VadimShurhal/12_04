import time

from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage


class HomePage(BasePage):


    # CONTACTS_TAB = (By.XPATH, "//a[@class='site-nav-link'][@href='https://kyiv.ithillel.ua/contact']")
    CONTACTS_TAB = (By.XPATH, "//*[@id='body']/div[1]/div[1]/div[2]/div/div/nav/ul/li[5]/a")
    DROP_DOWN = (By.XPATH, )


    def check_title(self):
        return self.check_title_on_page("Комп'ютерна школа Hillel у Києві: Курси IT-технологій")

    def click_on_contacts(self):
        time.sleep(2)
        self.find(self.CONTACTS_TAB).click()

    def click_review_in_drop_down(self, dropdown_name, element):
        return self.click_element_in_dropdown(dropdown_name, element)


