from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header_title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.add_to_cart_backpack = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']")
        self.remove_backpack = page.locator(
            "[data-test='remove-sauce-labs-backpack']")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.item_names = page.locator(".inventory_item_name")

    def is_inventory_page_visible(self):
        return self.header_title.is_visible()

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def get_cart_count(self):
        if not self.cart_badge.is_visible():
            return 0
        return int(self.cart_badge.inner_text())

    def sort_items(self, option):
        self.sort_dropdown.select_option(option)

    def get_first_item_name(self):
        return self.item_names.first.inner_text()
