from dataclasses import dataclass
from typing import Self
from playwright.sync_api import Page
from .inventory_page import InventoryPage


@dataclass
class Selectors:
    input_username: str = 'input[data-test="username"]'
    input_password: str = 'input[data-test="password"]'
    login_button: str = 'input[data-test="login-button"]'
    error_box: str = 'h3[data-test="error"]'


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.s = Selectors()

    def do_login(self, username: str, password: str) -> Self | InventoryPage:
        self.page.locator(self.s.input_username).fill(username)
        self.page.locator(self.s.input_password).fill(password)
        self.page.locator(self.s.login_button).click()
        if self.page.url == 'https://www.saucedemo.com/inventory.html':
            return InventoryPage(self.page)
        return LoginPage(self.page)
