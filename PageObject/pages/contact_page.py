from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage


class ContactPage(BasePage):

    CHAT_BUTTON = (By.XPATH, "//div[@class='hcw-widget-button _add-gradient _style-squared _type-icon']")
    CHAT_WINDOW = (By.XPATH, "//div[@class='hcw-widget__chat']")

    def check_title(self):
        return self.check_title_on_page("Контакти Комп'ютерної школи Hillel у Києві")

    def click_on_chat_button(self):
        self.find(self.CHAT_BUTTON).click()

    def check_chat_is_visible(self):
        self.wait_for(self.CHAT_WINDOW)
