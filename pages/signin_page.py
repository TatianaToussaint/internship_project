from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import Page


class SigninPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input#email-2[type="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input#field[type="password"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def input_credentials(self):
        email = 'donrabu@gmail.com'
        password = 'Tatiana0510$'
        self.input(email, *self.EMAIL_FIELD)
        sleep(2)
        self.input(password, *self.PASSWORD_FIELD)
        sleep(2)

    def click_continue(self):
        self.click(*self.CONTINUE_BUTTON)
