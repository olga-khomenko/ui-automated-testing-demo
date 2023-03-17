from dataclasses import dataclass
from playwright.sync_api import Page
from infrastructure.pages.cart import CartPage


@dataclass
class Selectors:
    menu: str = 'button[id="react-burger-menu-btn"]'
    close_menu: str ='button[id="react-burger-cross-btn"]'
    logout: str = 'a[id="logout_sidebar_link"]'
    cart: str = 'a[class="shopping_cart_link"]'
    add_to_cart: str = 'button[data-test="add-to-cart-test.allthethings()-%s"]'


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.s = Selectors()

    @property
    def open_menu(self):
        self.page.locator(self.s.menu).click()
        self.page.locator(self.s.close_menu).wait_for()

    def do_logout(self):
        from .login import LoginPage
        self.open_menu
        self.page.locator(self.s.logout).click()
        return LoginPage(self.page)

    def add_to_cart(self, item: str):
        self.page.locator(self.s.add_to_cart % item).scroll_into_view_if_needed()
        self.page.locator(self.s.add_to_cart % item).click()

    @property
    def open_cart(self) -> CartPage:
        self.page.locator(self.s.cart).click()
        return CartPage(self.page)

