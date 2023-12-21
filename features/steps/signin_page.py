from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_login(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(5)


@when('Log in to the page')
def login_to_the_page(context):
    context.app.signin_page.input_credentials()
    context.app.signin_page.click_continue()
    sleep(5)


# @then('Click on Continue')
# def click_continue(context):
#     context.app.signin_page.click_continue()

