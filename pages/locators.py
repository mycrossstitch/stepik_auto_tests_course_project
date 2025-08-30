from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form1")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form1")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
