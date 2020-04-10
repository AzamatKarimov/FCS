from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage): 
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        
    def check_alert_product_added(self,product_name):
        expected_alert=product_name+' has been added to your basket.'
        alert = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)[0].text
        assert expected_alert in alert, f"Should be '{expected_alert}' in alert:'{alert}'"

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
    def check_alert_sum_in_basket(self,price):
        expected_alert='Your basket total is now '+price
        alert = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)[2].text
        assert expected_alert in alert, f"Should be '{expected_alert}' in alert:'{alert}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should not disappear"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should disappear"