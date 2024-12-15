from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)

    def wait_for(self, condition, timeout=30):
        """Wait for a specified condition."""
        return WebDriverWait(self.driver, timeout).until(condition)

    def click_element(self, element):
        """Click a web element after ensuring it’s clickable."""
        locator = self.wait_for(EC.element_to_be_clickable(element))
        locator.click()

    def submit_element(self, element):
        locator = self.wait_for(EC.visibility_of_element_located(element))
        locator.submit()
    def send_element_text(self, element, text):
        """Send text to a web element."""
        #locator = self.wait_for(EC.element_to_be_clickable(element))
        locator = self.wait_for(EC.visibility_of_element_located(element))
        locator.clear()
        locator.send_keys(text)

    def find_element(self, element):
        return self.wait_for(EC.presence_of_element_located(element))

    def get_element(self,element):
        locator = self.wait_for(EC.presence_of_element_located(element))
        return locator.text

    def wait_element_visibility(self, element):
        """Wait for an element to be visible."""
        return self.wait_for(EC.visibility_of(element))

    def wait_element_invisibility(self, element):
        """Wait for an element to be visible."""
        return self.wait_for(EC.invisibility_of_element(element))

    def is_element_present(self, element):
        try:
            self.wait_for(EC.visibility_of_element_located(element))
            return True
        except (NoSuchElementException,TimeoutException):
            return False

    def wait_elements_visibility(self, elements):
        """Wait for elements to be visible."""
        self.wait_for(EC.visibility_of_all_elements_located(elements))

    # def get_elements_text(self, elements):
    #     """Validate multiple elements and return their texts."""
    #     texts = []
    #     for element in elements:
    #         locator = self.wait_for(EC.presence_of_element_located(element))
    #         if locator:
    #             texts.append(locator.text)
    #         else:
    #             texts.append(None)  # If element is not found, append None
    #     return texts

    def get_attribute_element(self, element , attribute):
       locator = self.find_element(element)
       attributeName = locator.get_attribute(attribute)
       print(f"Attribute value: {attributeName}")
       return attributeName