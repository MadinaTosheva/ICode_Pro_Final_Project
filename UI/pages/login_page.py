from selenium.webdriver.common.by import By
from UI.pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME  = (By.ID, 'user-name')
    PASSWORD  = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        return super().open("/")

    def login_as(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)


    def error_text(self) -> str:
        return self.text_of(self.ERROR_MSG)
