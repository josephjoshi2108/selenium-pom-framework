from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.get_title() == "Products"


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    assert "Username and password do not match" in login_page.get_error_message()


def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"