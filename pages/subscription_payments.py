from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import Page


class SubscriptionPaymentsPage(Page):
    SETTING_BUTTON = (By.CSS_SELECTOR, "a.menu-button-block[href*=set]")
    SUB_PAYMENT_BUTTON = (By.CSS_SELECTOR, "a[href='/subscription']")
    TITLE_PAGE = (By.CSS_SELECTOR, "[class='lotion-your-h3--price size']")
    UPGRADE_PLAN_BUTTON = (By.CSS_SELECTOR, "[class='button-verify  w-inline-block']")
    BACK_BUTTON = (By.CSS_SELECTOR, "[class='button-verify margin-top-8 white w-inline-block']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_setting_button(self):
        self.click(*self.SETTING_BUTTON)

    def click_sub_payment_button(self):
        self.wait_for_element_clickable(self.SUB_PAYMENT_BUTTON)

    def verify_title(self):
        self.wait_for_element_appear(self.TITLE_PAGE)
        self.verify_text('Subscription & payments', *self.TITLE_PAGE)

    def upgrade_plan_button_displayed(self):
        self.wait_for_element_appear(self.UPGRADE_PLAN_BUTTON)

    def back_button_displayed(self):
        self.wait_for_element_appear(self.BACK_BUTTON)
