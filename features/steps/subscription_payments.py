from behave import then


@then('Click on settings option')
def click_setting_button(context):
    context.app.click_setting_button()


@then('Click on Subscription & payments option')
def click_sub_payment_button(context):
    context.app.click_sub_payment_button()


@then('Verify the right page opens')
def verify_title(context):
    context.app.verify_title()


@then('Verify title “Subscription & payments” is visible')
def upgrade_plan_button_displayed(context):
    context.app.upgrade_plan_button_displayed()


@then('Verify “back” and “upgrade plan” buttons are available')
def back_button_displayed(context):
    context.app.back_button_displayed()
