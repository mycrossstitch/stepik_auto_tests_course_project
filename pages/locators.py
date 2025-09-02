from selenium.webdriver.common.by import By

class MainPageLocators():
    pass   # не используем,

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")  # ссылка на корзину в шапке
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")  # товары в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")  # сообщение о пустой корзине