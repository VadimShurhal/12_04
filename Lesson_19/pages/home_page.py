import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Lesson_19.constants import GithubTitles
from Lesson_19.pages.base_page import BasePage


class HomePage(BasePage):

    LOGIN_BUTTON = (By.LINK_TEXT, "Sign in")

    @allure.step('Check title on home page')
    def check_title(self):
        return self.check_title_on_page(GithubTitles.HOME_PAGE_TITLE)

    @allure.step('Click login button')
    def click_login_button(self):
        self.wait_for(self.LOGIN_BUTTON).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        # allure.attach.file('1.pdf', name="my_pdf_file", attachment_type=AttachmentType.PDF)




