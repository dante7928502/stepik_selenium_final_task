from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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