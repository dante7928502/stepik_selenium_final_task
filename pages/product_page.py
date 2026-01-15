from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BTN
        )
        add_to_basket_btn.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_name_in_notify(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_NOTIFY
        ).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def should_be_correct_product_name_in_notify(self):
        product_name = self.get_product_name()
        product_name_in_notify = self.get_product_name_in_notify()

        assert (
            product_name == product_name_in_notify
        ), f'Expected "{product_name}" in notify, but got "{product_name_in_notify}"'

    def should_be_correct_basket_price(self):
        product_price = self.get_product_price()
        basket_price = self.get_basket_price()

        assert (
            product_price == basket_price
        ), f'Expected basket price "{product_price}", but got "{basket_price}"'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def success_msg_is_dissapeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message should dissapear, but it's still here"
