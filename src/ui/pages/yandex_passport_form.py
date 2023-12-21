from src.selenium.base_page import BasePage
from src.selenium.locator import Locator
from time import sleep

class YandexPassportForm(BasePage):
    URL = 'https://passport.yandex.ru/'
    LOGIN_WITH_YANDEX_ID = Locator(
        name="название формы авторизации",
        locator="//span[contains(text(), 'Войдите')]"
    )
    EMAIL_TAB_BUTTON = Locator(
        name="кнопка переключения таба 'Почта'",
        locator="//button[@data-type='login']"
    )
    PHONE_TAB_BUTTON = Locator(
        name="кнопка переключения таба 'Телефон'",
        locator="//button[@data-type='phone']"
    )
    LOGIN_INPUT = Locator(
        name="поле для ввода email",
        locator="//input[@id='passp-field-login']"
    )
    PHONE_INPUT = Locator(
        name="поле для ввода номера телефона",
        locator="//input[contains(@id, 'passp-field-phone')]"
    )
    SING_IN_BUTTON = Locator(
        name="кнопка 'Войти'",
        locator="//button[@id='passp:sign-in']"
    )
    PHONE_HINT = Locator(
        name="подсказка для номера телефона",
        locator="//div[contains(@id, 'field:input-phone:hint')]"
    )
    LOGIN_HINT = Locator(
        name="подсказка для email",
        locator="//div[contains(@id, 'field:input-login:hint')]"
    )

    def open_current_page(self):
        self.open_page(self.URL)

    def enter_email(self, email: str) -> bool:
        self.click_on_element(self.EMAIL_TAB_BUTTON)
        self.find_element(self.LOGIN_INPUT).send_keys(email)
        self.click_on_element(self.SING_IN_BUTTON)
        self.find_visible_element(self.LOGIN_HINT)
        return True

    def enter_phone_number(self, phone: str = '') -> bool:
        self.click_on_element(self.PHONE_TAB_BUTTON, 15)
        self.find_element(self.PHONE_INPUT).send_keys(phone)
        self.click_on_element(self.SING_IN_BUTTON)
        return True

