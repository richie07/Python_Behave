from behave import *
from pages.Login_Page import LoginPage

@given(u'launch on page home')
def launchBrowser(context):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.visit(context.base_url)

@step(u'the user enters "{username}" in Nombre field and "{password}" in password field')
def step_impl(context, username, password):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.type_userNameAndPassword(username, password)


@step(u'the user clicks the "Acceder" button')
def step_impl(context):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.click_submit_button()
