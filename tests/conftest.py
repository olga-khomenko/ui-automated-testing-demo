from playwright.sync_api import Page
from pytest import fixture

from infrastructure.pages.inventory import InventoryPage
from infrastructure.pages.login import LoginPage


@fixture
def login_page(page: Page) -> LoginPage:
    page.goto('https://www.saucedemo.com')
    return LoginPage(page)


@fixture
def inventory_page(login_page) -> InventoryPage:
    return login_page.do_login(username='standard_user', password='secret_sauce')
