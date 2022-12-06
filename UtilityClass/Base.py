from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Base():

    def __init__(self, driver):
        self.driver = driver
    
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendkeys(self, by_locator, txt):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(txt)

    def get_element_txt(self, by_locator, txt):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


#     def test_setup(self, driver):
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option('excludeSwitches', ['enable-logging'])
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.maximize_window()

#     def login(self):
#         self.driver.get("http://www.python.org")  


#     def tearDown(self):
#         self.driver.close()
    
#     def show(self):
#         print(self.driver)

# test = Utilities()
# # test.test_setup(ChromeDriverManager)
# # test.login()
# test.show()


