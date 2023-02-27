import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(500)
    page.should_success_message_exists()
    title_of_item = page.get_title_of_item()
    page.should_be_success_message_for_add_to_basket(title_of_item)
