from playwright.sync_api import Page
from pytest import fixture

from infrastructure.pages.login import LoginPage


@fixture
def login_page(page: Page) -> LoginPage:
    page.goto('https://www.saucedemo.com')
    return LoginPage(page)