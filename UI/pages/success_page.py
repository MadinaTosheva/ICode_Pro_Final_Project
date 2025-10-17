from UI.pages.base_page import BasePage



class SuccessPage(BasePage):


    def success_message(self, message) -> bool:
        return message in self.browser.current_url