from dataclasses import dataclass
from playwright.sync_api import Page


@dataclass
class Selectors:
    title: str = 'span[class="title"]'


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.s = Selectors()
