from behave import *
from pages.List_User_Page import ListUserPage

@then(u'the user can see the new user create "{user}"')
def step_impl(context, user):
    context.listUserPage = ListUserPage(context.driver)
    assert True == context.listUserPage.find_nameCreateExist(user)


@step(u'the user clicks in borrar "{user}" user')
def step_impl(context, user):
    context.listUserPage = ListUserPage(context.driver)
    context.listUserPage.delete_UserName(user)


@when(u"the user clicks in confirmar borrado button")
def step_impl(context):
    context.listUserPage = ListUserPage(context.driver)
    context.listUserPage.click_ConfirmarBorrado()


@then(u'the user can\'t see "{user}" user')
def step_impl(context, user):
    context.listUserPage = ListUserPage(context.driver)
    assert False == context.listUserPage.find_nameCreateExist(user)