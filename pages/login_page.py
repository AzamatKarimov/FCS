from .base_page import BasePage
from .locators import LoginPageLocators
import pytest

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Login URL is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Reg form is not presented"
        assert True
           
    def register_new_user(self, email, password):
        register_new_user_email = self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        register_new_user_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password)
        register_new_user_password2 = self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT).click()
        #return_to_home_page = self.browser.find_element(*LoginPageLocators.RETURN_TO_HOME_PAGE).click()
        
