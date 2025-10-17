import time

import pytest
from UI.pages.checkout_page import CheckoutPage
from UI.pages.inventory_page import InventoryPage
from UI.pages.login_page import LoginPage
from UI.pages.confirm_page import ConfirmPage
from UI.pages.success_page import SuccessPage


class TestPurchase:

    @pytest.mark.regress
    def test_purchase_success(self, browser,  login_page: LoginPage, inventory_page: InventoryPage, checkout_page: CheckoutPage, confirm_page: ConfirmPage, success_page: SuccessPage ):

        (login_page
         .open()
         .login_as("standard_user", "secret_sauce"))
        assert inventory_page.url_contains("inventory")

        (inventory_page
         .add_to_cart()
         .click_shopping_container())
        assert checkout_page.url_contains("cart")

        (checkout_page
         .go_to_checkout()
         .fill_user_info("Jon", "Smith", "1234"))

        time.sleep(5)
        confirm_page.finish_the_payment()
        time.sleep(10)

        assert  success_page.success_message("checkout-complete")