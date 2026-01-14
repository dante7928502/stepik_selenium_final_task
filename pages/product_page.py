from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BTN
        )
        add_to_basket_btn.click()

    def find_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def find_product_name_in_notify(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_NOTIFY
        ).text

    def find_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def find_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def should_not_be_success_message(self):
        return self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def success_msg_is_dissapeared(self):
        return self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
