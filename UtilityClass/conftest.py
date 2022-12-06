
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def init_driver(browsername):
    if browsername == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if browsername == "firefox":
        web_driver = webdriver.Chrome(executable_path=GeckoDriverManager().install())
    
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()

