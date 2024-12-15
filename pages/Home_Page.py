from pages.Base_Page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    txtBienvenida = (By.XPATH, "//h2[contains(text(),'¡Te damos la bienvenida a WordPress!')]")
    lblError = (By.ID, "login_error")
    btnUsuarios = (By.CSS_SELECTOR, "#menu-users > a")
    btnAñadirNuevoUsuario = (By.CSS_SELECTOR,"li#menu-users > ul:first-of-type > li:nth-child(3) > a")
    btnAllUsuarios = (By.CSS_SELECTOR, "#menu-users > ul > li:nth-of-type(2) > a")

    def __init__(self, driver):
        super().__init__(driver)

    def getTextWelcome(self):
        return self.get_element(self.txtBienvenida)

    def isVisibleError(self):
        return self.is_element_present(self.lblError)

    def clickMenuUsuarios(self):
        self.click_element(self.btnUsuarios)

    def clickMenuAñadirNuevoUsuario(self):
        self.click_element(self.btnAñadirNuevoUsuario)

    def clickMenuAllUsuarios(self):
        self.click_element(self.btnAllUsuarios)

