import pytest
from playwright.sync_api import expect
from config.config import Config


@pytest.mark.ui
class TestSauceDemoUI:

    # Test 1: Happy Path - Login successful
    def test_valid_login(self, login_page, inventory_page):
        login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        expect(inventory_page.header_title).to_have_text("Products")

    # Test 2: Negative - Locked out user
    def test_locked_out_user(self, login_page):
        login_page.login(Config.LOCKED_OUT_USER, Config.PASSWORD)
        expect(login_page.error_message).to_contain_text(
            "Sorry, this user has been locked out")

    # Test 3: State Change - Add to cart updates badge
    def test_add_to_cart_badge(self, login_page, inventory_page):
        login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        assert inventory_page.get_cart_count() == 0
        inventory_page.add_backpack_to_cart()
        expect(inventory_page.cart_badge).to_have_text("1")

    # Test 4: Sorting Functionality (State Change)
    def test_sort_z_to_a(self, login_page, inventory_page):
        login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        inventory_page.sort_items("za")  # Name (Z to A)
        assert inventory_page.get_first_item_name() == "Test.allTheThings() T-Shirt (Red)"

    # Test 5: Logout (Flow)
    def test_logout(self, login_page, page):
        login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        page.locator("#react-burger-menu-btn").click()
        page.locator("#logout_sidebar_link").click()
        expect(login_page.login_button).to_be_visible()
