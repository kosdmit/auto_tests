from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_success_message_exists(self):
        self.success_messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        assert len(self.success_messages) != 0, "Success message did not found on the product page"

    def should_be_success_message_for_add_to_basket(self, title_of_item):
        flag = False
        for message in self.success_messages:
            if title_of_item + " has been added to your basket." == message.text:
                print(message.text)
                flag = True
        assert flag, "Success message did not found on the product page"

    def get_title_of_item(self):
        title = self.browser.find_element(*ProductPageLocators.ITEM_TITLE)
        return title.text

    def get_price_of_item(self):
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        return price.text



