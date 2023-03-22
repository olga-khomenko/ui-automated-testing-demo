from dataclasses import dataclass
from playwright.sync_api import Page

from infrastructure.pages.checkout import CheckoutPage


@dataclass
class Selectors:
    title: str = 'span[class="title"]'
    item: str = 'div[class="inventory_item_name"]:has-text("%s")'
    checkout_button: str = 'button[data-test="checkout"]'
    remove_button: str = 'button[data-test="remove-%s"]'


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.s = Selectors()

    def do_checkout(self) -> CheckoutPage:
        self.page.locator(self.s.checkout_button).click()
        return CheckoutPage(self.page)

    def remove_item(self, item: str):
        self.page.locator(self.s.remove_button % item).click()

    def displays_item(self, item: str) -> bool:
        return self.page.locator(self.s.item % item).is_visible()
