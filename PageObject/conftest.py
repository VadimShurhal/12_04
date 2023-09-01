
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True, scope='session')
def driver():
    # setup
    PATH = r'C:\Users\vadym.shurkhal\Desktop\hillel\12_04\Lesson_17\driver\chromedriver.exe'
    driver = webdriver.Chrome(service=Service(PATH))
    driver.implicitly_wait(2)
    driver.get('https://kyiv.ithillel.ua/')
    driver.maximize_window()
    yield driver
    driver.quit()