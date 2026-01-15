from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import faker

@pytest.mark.need_review
@pytest.mark.parametrize(
    "link_promo",
    [
        "/?promo=offer0",
        # "/?promo=offer1",
        # "/?promo=offer2",
        # "/?promo=offer3",
        # "/?promo=offer4",
        # "/?promo=offer5",
        # "/?promo=offer6",
        pytest.param(
            "/?promo=offer7",
            marks=pytest.mark.xfail(reason="nobody planning to fix it"),
        ),
        # "/?promo=offer8",
        # "/?promo=offer9",
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
    product_page.should_be_correct_product_name_in_notify()
    product_page.should_be_correct_basket_price()


@pytest.mark.xfail(reason="that is negative check")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="that is negative check")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.success_msg_is_dissapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_is_empty_notify()

@pytest.fixture(scope="function")
def register_user(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    email = faker.Faker().email(domain="dante7928.com")
    password = faker.Faker().password(length=10)

    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.register_new_user(email, password)
    login_page.should_be_authorized_user()

@pytest.mark.usefixtures("register_user")
class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.should_be_correct_product_name_in_notify()
        product_page.should_be_correct_basket_price()
