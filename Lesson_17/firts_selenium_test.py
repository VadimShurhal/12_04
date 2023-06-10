import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


# if chromedriver in PATH
# driver = webdriver.Chrome()

# # set path to chromedriver
# PATH = r'C:\Users\vadym.shurkhal\Desktop\hillel\12_04\Lesson_17\driver\chromedriver.exe'
# driver = webdriver.Chrome(service=Service(PATH))
#
# driver manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# sleeps
driver.implicitly_wait(2)
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException])


driver.get("https://www.google.com")
# time.sleep(2)

search_field = driver.find_element(By.NAME, 'q')
search_field.send_keys('hillel')
# time.sleep(2)

print(driver.title)
print(driver.name)
print(driver.current_url)

# first_in_list = driver.find_element(By.XPATH, '//*[@id="Alh6id"]/div[1]/div/ul/li[1]')
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Alh6id"]/div[1]/div/ul/li[1]'))).click()

assert '/search' in driver.current_url

search_list = driver.find_elements(By.XPATH, "//h3")
for item in search_list:
    print(item.text)
    if item.text == 'О школе':
        item.click()
        time.sleep(2)


#driver.close()
driver.quit()