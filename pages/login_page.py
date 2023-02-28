from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, f"'login' is not in current url - " \
                                                    f"'{self.browser.current_url}'."

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, 'Login form is not founded on the page'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form, 'Register form is not founded on the page'

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys(password)

        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()
