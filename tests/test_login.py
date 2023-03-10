from playwright.sync_api import Page


class TestLogin:

    def test_valid_login(self, page: Page):
        page.goto("https://www.saucedemo.com")
        page.locator('input[data-test="username"]').fill('standard_user')
        page.locator('input[data-test="password"]').fill('secret_sauce')
        page.locator('input[data-test="login-button"]').click()

        assert page.url == "https://www.saucedemo.com/inventory.html"
