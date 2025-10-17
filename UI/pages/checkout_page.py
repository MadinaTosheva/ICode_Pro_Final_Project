from selenium.webdriver.common.by import By
from UI.pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRSTNAME  = (By.ID, 'first-name')
    LASTNAME  = (By.ID, 'last-name')
    POSTALCODE = (By.ID, 'postal-code')
    CHECKOUT_BTN = (By.ID, 'checkout')
    CONTINUE_BTN = (By.ID, 'continue')
    FINISH_BTN = (By.ID, 'finish')

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BTN)
        return self

    def fill_user_info(self, firstname: str, lastname: str, postalcode: str):
        self.type(self.FIRSTNAME, firstname)
        self.type(self.LASTNAME, lastname)
        self.type(self.POSTALCODE, postalcode)
        self.click(self.CONTINUE_BTN)
        return self


    def url_contains(self, path) -> bool:
      return path in self.browser.current_url