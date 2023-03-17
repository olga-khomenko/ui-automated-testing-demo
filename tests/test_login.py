
class TestLogin:

    def test_valid_login(self, login_page):
        inventory = login_page.do_login(username='standard_user', password='secret_sauce')

        assert inventory.page.url == 'https://www.saucedemo.com/inventory.html'

    def test_invalid_password(self, login_page):
        expected_error = 'Epic sadface: Username and password do not match any user in this service'
        login = login_page.do_login(username='standard_user', password='blahblahblah')

        assert login.page.url == 'https://www.saucedemo.com/'
        assert login.page.locator(login_page.s.error_box).inner_text() == expected_error

    def test_empty_password(self, login_page):
        expected_error = 'Epic sadface: Password is required'
        login = login_page.do_login(username='standard_user', password='')

        assert login.page.url == 'https://www.saucedemo.com/'
        assert login.page.locator(login_page.s.error_box).inner_text() == expected_error

    def test_invalid_username(self, login_page):
        expected_error = 'Epic sadface: Username and password do not match any user in this service'
        login = login_page.do_login(username='blahblahblah', password='secret_sauce')

        assert login.page.url == 'https://www.saucedemo.com/'
        assert login.page.locator(login_page.s.error_box).inner_text() == expected_error

    def test_empty_username(self, login_page):
        expected_error = 'Epic sadface: Username is required'
        login = login_page.do_login(username='', password='secret_sauce')

        assert login.page.url == 'https://www.saucedemo.com/'
        assert login.page.locator(login_page.s.error_box).inner_text() == expected_error

    def test_empty_username_and_empty_password(self, login_page):
        expected_error = 'Epic sadface: Username is required'
        login = login_page.do_login(username='', password='')

        assert login.page.url == 'https://www.saucedemo.com/'
        assert login.page.locator(login_page.s.error_box).inner_text() == expected_error


class TestLogout:

    def test_logout(self, login_page):
        inventory = login_page.do_login(username='standard_user', password='secret_sauce')
        login = inventory.do_logout

        assert login.page.url == 'https://www.saucedemo.com/'
