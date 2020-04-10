from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "input#id_registration-email") 
    PASSWORD1 = (By.CSS_SELECTOR, "input#id_registration-password1") 
    PASSWORD2 = (By.CSS_SELECTOR, "input#id_registration-password2") 
    BUTTON_SUBMIT = (By.NAME, "registration_submit") 
    RETURN_TO_HOME_PAGE = (By.CSS_SELECTOR, "div.col-sm-7") 
   
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasketPageLocators():
    PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "div.basket-items")
    DONT_PRODUCT_TO_BASKET = (By.XPATH, "Ваша корзина теперь пуста")
    ALERT = (By.CSS_SELECTOR, "div#content_inner>p") 
    
