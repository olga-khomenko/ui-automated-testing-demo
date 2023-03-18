

class TestCart:

    def test_checkout_cart(self, inventory_page):
        inventory_page.add_to_cart(item='t-shirt-(red)')
        cart = inventory_page.open_cart
        checkout_page = cart.do_checkout()
        checkout_page.enter_customer_data('John', 'Doe', '25480')
        checkout_page.click_continue()
        checkout_page.click_finish()

        assert checkout_page.title_value_is('Checkout: Complete!')
        assert checkout_page.header_value_is('Thank you for your order!')
