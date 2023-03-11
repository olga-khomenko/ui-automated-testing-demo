from typing import Self
from playwright.sync_api import Page
from ..page_objects.inventory_page import InventoryPage

input_username = 'input[data-test="username"]'
input_password = 'input[data-test="password"]'
login_button = 'input[data-test="login-button"]'
error_box = 'h3[data-test="error"]'


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def do_login(self, username: str, password: str) -> Self | InventoryPage:
        self.page.locator(input_username).fill(username)
        self.page.locator(input_password).fill(password)
        self.page.locator(login_button).click()
        if self.page.url == 'https://www.saucedemo.com/inventory.html':
            return InventoryPage(self.page)
        return LoginPage(self.page)
