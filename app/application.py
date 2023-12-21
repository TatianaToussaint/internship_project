from pages.base_page import Page
from pages.signin_page import SigninPage
from pages.subscription_payments import SubscriptionPaymentsPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.signin_page = SigninPage(driver)
        self.subscription_payments_page = SubscriptionPaymentsPage(driver)
