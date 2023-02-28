from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SELECTED_LANGUAGE = (By.CSS_SELECTOR, 'select[name="language"] option[selected="selected"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success div.alertinner")
    ITEM_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')


class BasketPageLocators():
    ITEM = (By.CSS_SELECTOR, 'div.basket-items div')
    MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')