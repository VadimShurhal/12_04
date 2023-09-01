import time

from PageObject.pages.contact_page import ContactPage
from PageObject.pages.home_page import HomePage


def test_hillel(driver):
    home_page = HomePage(driver)
    home_page.check_title()
    time.sleep(3)
    home_page.click_review_in_drop_down('Школа', 'Відгуки')
    time.sleep(3)


    # contact_page = ContactPage(driver)
    # contact_page.check_title()
    # contact_page.click_on_chat_button()
    # contact_page.check_chat_is_visible()