from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, base_url, timeout: int = 20):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, timeout)

    def open(self, path=""):
        url = f"{self.base_url}{path}"
        self.browser.get(url)
        return  self


    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))


    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


    def click(self, locator):
        return  self.wait.until(EC.element_to_be_clickable(locator)).click()


    def type(self, locator, text):
        return self.visible(locator).send_keys(text)


    def text_of(self, locator):
        return self.visible(locator).text