from selenium.webdriver.common.by import By
from pages.Base_Page import BasePage

class LoginPage(BasePage):
    txtUserName = (By.ID, "user_login")
    txtPassword = (By.ID, "user_pass")
    btnSubmit = (By.ID, "wp-submit")

    def __init__(self, driver):
        super().__init__(driver)

    def type_userNameAndPassword(self, userName, password):
        self.send_element_text(self.txtUserName, userName)
        self.send_element_text(self.txtPassword, password)

    def click_submit_button(self):
        self.click_element(self.btnSubmit)

