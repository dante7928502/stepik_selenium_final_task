from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_PRODUCT
        ), "Basket should be empty, but it's not"

    def basket_is_empty_notify(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_NOTIFY
        ), "Missing notify that basket is empty"

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "URL doesn't contain 'basket' part"
