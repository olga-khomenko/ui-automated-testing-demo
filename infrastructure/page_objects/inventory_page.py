from dataclasses import dataclass
from playwright.sync_api import Page


@dataclass
class Selectors:
    menu: str = 'button[id="react-burger-menu-btn"]'
    close_menu: str ='button[id="react-burger-cross-btn"]'
    logout: str = 'a[id="logout_sidebar_link"]'


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.s = Selectors()

    @property
    def open_menu(self):
        self.page.locator(self.s.menu).click()
        self.page.locator(self.s.close_menu).wait_for()

    @property
    def do_logout(self):
        from .login_page import LoginPage
        self.open_menu
        self.page.locator(self.s.logout).click()
        return LoginPage(self.page)
