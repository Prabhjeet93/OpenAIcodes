from UtilityClass.Base import Base
from selenium.webdriver.common.by import By
class Loginpage(Base):

    Email = (By.ID, "username")
    password = (By.ID, "password")
    btn_login = (By.ID, "submit")




    def __init__(self, driver):
        super.__init__(driver)
        
    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, passwd):
        self.do_sendkeys(self.Email, username)
        self.do_sendkeys(self.password, passwd)
        self.do_click(self.btn_login)







