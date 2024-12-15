from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

def before_all(context):
    browser = context.config.userdata.get('browser','chrome')
    base_url = context.config.userdata.get('base_url','http://localhost:8080/wp-login.php')
    context.base_url = base_url
    context.driver = None

    if browser == "firefox":
        context.driver = webdriver.Firefox()
    elif browser == "chrome":
        context.driver = webdriver.Chrome()
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")

def after_all(context):
    if context.driver:
        context.driver.quit()