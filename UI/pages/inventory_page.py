from selenium.webdriver.common.by import By
from UI.pages.base_page import BasePage


class InventoryPage(BasePage):


    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-sauce-labs-backpack')
    SHOPPING_CONTAINER = (By.ID, 'shopping_cart_container')
    # FIRST_INVENTORY_ITEM_IMAGE = (By.XPATH, '//div[@class = "inventory_item_img"][1]')
    # FIRST_INVENTORY_ITEM_TITLE = (By.XPATH, '//div[@class ="inventory_item_name "][1]')
    # FIRST_INVENTORY_ITEM_PRICE = (By.XPATH, '//div[@class ="inventory_item_price"][1]')
    # CART_ITEM_TITLE = (By.XPATH, '//div[@class ="inventory_item_name"]')


    def url_contains(self, path) -> bool:
      return path in self.browser.current_url


    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        return self


    def click_shopping_container(self):
        self.click(self.SHOPPING_CONTAINER)
        return self






