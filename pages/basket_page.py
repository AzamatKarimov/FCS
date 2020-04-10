from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException
import pytest

class BasketPage(BasePage):  
    def should_not_be_product_to_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_TO_BASKET), "There should be no items in the list"
        
  #  def should_be_product_to_basket(self):
        #assert self.is_element_present(*BasketPageLocators.DONT_PRODUCT_TO_BASKET), "!!!DANGER!!!DANGER!!!"
      #  assert self.is_not_element_present(*BasketPageLocators.PRODUCT_TO_BASKET), "!!!DANGER!!!DANGER!!!"

    def text_basket_is_empty_should_be_present(self):
        #expected_alert='basket is empty'
        alert = self.browser.find_element(*BasketPageLocators.ALERT).text 
        assert 'basket is empty' in alert, "Text 'Basket is empty' should be present"


















    
    
