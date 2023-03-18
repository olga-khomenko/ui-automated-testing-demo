from dataclasses import dataclass
from playwright.sync_api import Page


@dataclass
class Selectors:
    title: str = 'span[class="title"]'
    first_name: str = 'input[data-test="firstName"]'
    last_name: str = 'input[data-test="lastName"]'
    postal_code: str = 'input[data-test="postalCode"]'
    continue_button: str = 'input[data-test="continue"]'
    cancel_button: str = 'button[data-test="cancel"]'
    finish_button: str = 'button[data-test="finish"]'
    complete_header: str = 'h2[class="complete-header"]'


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.s = Selectors()

    def enter_customer_data(self, first_name: str = None, last_name: str = None, postal_code: str = None):
        if first_name:
            self.page.locator(self.s.first_name).fill(first_name)
        if last_name:
            self.page.locator(self.s.last_name).fill(last_name)
        if postal_code:
            self.page.locator(self.s.postal_code).fill(postal_code)

    def click_continue(self):
        self.page.locator(self.s.continue_button).click()

    def click_cancel(self):
        self.page.locator(self.s.cancel_button).click()

    def click_finish(self):
        self.page.locator(self.s.finish_button).click()

    def title_value_is(self, text) -> bool:
        return self.page.locator(self.s.title).text_content() == text

    def header_value_is(self, text) -> bool:
        return self.page.locator(self.s.complete_header).text_content() == text
