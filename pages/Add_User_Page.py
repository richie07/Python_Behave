from selenium.webdriver.common.by import By
from pages.Base_Page import BasePage

class AddUserPage(BasePage):
    txtNombreUsuario = (By.ID, 'user_login')
    txtEmail = (By.ID, 'email')
    lblPassword = (By.CSS_SELECTOR, '#pass1')
    atrPassword = "data-pw"
    btnAñadirUsuario = (By.ID, 'createusersub')

    def __init__(self, driver):
        super().__init__(driver)

    def fillOutAñadirUsuarioNuevo(self,user ,email):
        self.send_element_text(self.txtNombreUsuario, user)
        self.send_element_text(self.txtEmail, email)

    def submitForm(self):
        self.submit_element(self.btnAñadirUsuario)

    def get_attribute_password(self):
        return self.get_attribute_element(self.lblPassword ,self.atrPassword)

