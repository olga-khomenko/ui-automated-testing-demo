from playwright.sync_api import Page


menu = 'button[id="react-burger-menu-btn"]'
close_menu ='button[id="react-burger-cross-btn"]'
logout = 'a[id="logout_sidebar_link"]'


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def open_menu(self):
        self.page.locator(menu).click()
        self.page.locator(close_menu).wait_for()

    @property
    def do_logout(self):
        from ..page_objects.login_page import LoginPage
        self.open_menu
        self.page.locator(logout).click()
        return LoginPage(self.page)
