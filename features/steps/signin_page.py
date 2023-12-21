from behave import given, when
from time import sleep


@given('Open the main page')
def open_login(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(5)


@when('Log in to the page')
def input_credentials(context):
    context.app.signin_page.input_credentials()
    sleep(5)


@when('Click on Continue')
def click_continue(context):
    context.app.signin_page.click_continue()

