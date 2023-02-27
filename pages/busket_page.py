from .base_page import BasePage
from .locators import BasketPageLocators


languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
        self.message = self.browser.find_element(*BasketPageLocators.MESSAGE)
    def should_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM)

    def should_be_message(self):
        assert self.message, "Message is not exists"

    def should_be_message_about_basket_is_empty(self):
        flag = False
        for key, value in languages.items():
            if value in self.message.text:
                flag = True
        assert flag, "Message about basket is empty does not found"