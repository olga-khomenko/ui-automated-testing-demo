from dataclasses import dataclass
from playwright.sync_api import Page

from infrastructure.pages.checkout import CheckoutPage

@dataclass
class Selectors:
    title: str = 'span[class="title"]'
    checkout_button: str = 'button[data-test="checkout"]'


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.s = Selectors()

    def do_checkout(self) -> CheckoutPage:
        self.page.locator(self.s.checkout_button).click()
        return CheckoutPage(self.page)
