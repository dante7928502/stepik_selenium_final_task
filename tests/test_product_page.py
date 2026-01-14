from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.parametrize(
    "link_promo",
    [
        "/?promo=offer0",
        "/?promo=offer1",
        "/?promo=offer2",
        "/?promo=offer3",
        "/?promo=offer4",
        "/?promo=offer5",
        "/?promo=offer6",
        pytest.param(
            "/?promo=offer7",
            marks=pytest.mark.xfail(reason="nobody planning to fix it"),
        ),
        "/?promo=offer8",
        "/?promo=offer9",
    ],
)
def test_guest_can_add_product_to_basket(browser, link_promo):
    link = (
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        + link_promo
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()

    product_name = product_page.find_product_name()
    product_name_in_notify = product_page.find_product_name_in_notify()

    product_price = product_page.find_product_price()
    basket_price = product_page.find_basket_price()

    assert (
        product_name == product_name_in_notify
    ), f"Expected {product_name} in notify, but got {product_name_in_notify}"

    assert (
        product_price == basket_price
    ), f'Expected "Basket Price" = product price, but it\'s not'


@pytest.mark.xfail(reason="that is negative check")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    assert (
        product_page.should_not_be_success_message()
    ), "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert (
        product_page.should_not_be_success_message()
    ), "Success message is presented, but should not be"


@pytest.mark.xfail(reason="that is negative check")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    assert (
        product_page.success_msg_is_dissapeared()
    ), "Success message should dissapear, but it's still here"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.basket_is_empty(), "Basket should be empty, but it's not"
    assert (
        basket_page.basket_is_empty_notify()
    ), "Expected notify about empty basket, but didn't get any"
