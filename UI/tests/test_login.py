import pytest

from UI.pages.inventory_page import InventoryPage
from UI.pages.login_page import LoginPage


class TestLoginPage:

    @staticmethod
    @pytest.mark.smoke
    def test_login_success(self, login_page: LoginPage, inventory_page: InventoryPage):
        (login_page
         .open()
         .login_as("standard_user", "secret_sauce"))
        assert inventory_page.url_contains ("inventory")

    @pytest.mark.negative
    def test_login_wrong_password(self, login_page: LoginPage):
        (login_page
         .open()
         .login_as("standard_user", "no_secret_sauce"))
        assert "Epic sadface: Username and password do not match any user in this service" in login_page.error_text()

    @pytest.mark.negative
    def test_login_empty_fields(self, login_page: LoginPage):
        (login_page
         .open()
         .login_as("", ""))
        assert "Epic sadface: Username is required" in login_page.error_text()


    @pytest.mark.negative
    def test_login_locked_out_user(self, login_page: LoginPage):
        (login_page
         .open()
         .login_as("locked_out_user", "secret_sauce"))
        assert "Epic sadface: Sorry, this user has been locked out." in login_page.error_text()


    def test_login_problem_user(self, login_page: LoginPage, inventory_page: InventoryPage):
        (login_page
         .open()
         .login_as("problem_user", "secret_sauce"))





