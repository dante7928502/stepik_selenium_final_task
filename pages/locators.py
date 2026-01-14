from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_NOTIFY = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_NOTIFY = (
        By.CSS_SELECTOR,
        "#messages > div:nth-child(1) > div > strong",
    )
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    BASKET_PRICE = (
        By.CSS_SELECTOR,
        "#messages > div.alert-safe > div > p:nth-child(1) > strong",
    )
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
