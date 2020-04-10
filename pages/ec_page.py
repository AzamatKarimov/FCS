from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class EcPage(BasePage):
    #def should_be_basket(self):
          #  buttom3 = self.browser.find_element(*ProductPageLocators.Basket_click).click()
           # page = BasePage(self.browser, self.url)
            #page.solve_quiz_and_get_code()
    
    def should_not_be_success_message(self): #метод проверяющий что сообщение не появляется заднное время
        #buttom3 = self.browser.find_element(*ProductPageLocators.Basket_click).click()
        page = BasePage(self.browser,self.url)
        #page.solve_quiz_and_get_code()
        page.is_not_element_present
        #page.is_disappeared
        print(11)
        message_2 = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        print (message_2)
        #assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        print(22)
       
    #def should_not_be_success_message(self):
       #assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    #def should_not_be_success_message(self):
     #   assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should not disappear"