class TestSales:

    def test_add_red_tshirt_to_cart(self, inventory_page):
        inventory_page.add_to_cart(item='t-shirt-(red)')
        cart = inventory_page.open_cart

        assert cart.page.locator(cart.s.title).text_content() == 'Your Cart'
