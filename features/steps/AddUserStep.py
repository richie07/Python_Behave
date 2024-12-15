from behave import *
from pages.Add_User_Page import AddUserPage

@step(u'the user fill in "{name}" in Nombre de usuario field and "{email}" in Correo electrónico field')
def step_impl(context,name,email):
    context.AddUserPage = AddUserPage(context.driver)
    context.AddUserPage.fillOutAñadirUsuarioNuevo(user=name,email=email)
    context.AddUserPage.get_attribute_password()


@when(u"the user clicks in Añadir nuevo usuario button")
def step_impl(context):
    context.AddUserPage = AddUserPage(context.driver)
    context.AddUserPage.submitForm()