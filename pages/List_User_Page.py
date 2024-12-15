from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.Base_Page import BasePage

class ListUserPage(BasePage):
    lstNames = (By.XPATH , '//tbody[@id="the-list"]//td[@data-colname="Nombre de usuario"]/strong/a')
    lstEmails = (By.XPATH, "//tbody[@id='the-list']//td[@data-colname='Correo electrónico']/a")
    lstNameDelete = (By.XPATH ,'//tbody[@id="the-list"]//td[@data-colname="Nombre de usuario"]/strong/a[text()="{text}"]/parent::strong/following-sibling::div/span/a[@class="submitdelete"]')
    btnConfimarBorrado = (By.ID,'submit')

    def __init__(self, driver):
        super().__init__(driver)

    def find_nameCreateExist(self, name_to_search):
        self.wait_elements_visibility(self.lstNames)
        names_list = self.driver.find_elements(*self.lstNames)
        names = [names.text for names in names_list]
        if name_to_search in names:
            return True
        else:
            return False

    def delete_UserName(self, name_to_delete):
        xpath = self.lstNameDelete[1].format(text=name_to_delete)
        locatorDelete = (self.lstNameDelete[0], xpath)
        element = self.find_element(locatorDelete)
        self.driver.execute_script("arguments[0].click();", element)
        #ActionChains(self.driver).move_to_element(element).perform()

    def click_ConfirmarBorrado(self):
        self.submit_element(self.btnConfimarBorrado)

