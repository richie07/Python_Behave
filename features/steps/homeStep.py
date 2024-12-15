from behave import *
from pages.Home_Page import HomePage

@then(u'the user should see the message "{text}"')
def step_impl(context,text):
    context.home_page = HomePage(context.driver)
    assert text == context.home_page.getTextWelcome()
@then(u"the user should see the message error")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert True == context.home_page.isVisibleError()
@step(u"the user clicks in Usuarios menu")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.clickMenuUsuarios()

@step(u"the user clicks in Añadir nuevo usuario")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.clickMenuAñadirNuevoUsuario()


@step("the user clicks in Todos los usuarios menu")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.clickMenuAllUsuarios()