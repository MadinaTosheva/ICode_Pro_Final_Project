import time

from selenium.webdriver.common.by import By
from UI.pages.base_page import BasePage


class ConfirmPage(BasePage):

    FINISH_BTN = (By.ID, 'finish')


    def finish_the_payment(self):
        self.click(self.FINISH_BTN)
        return self
