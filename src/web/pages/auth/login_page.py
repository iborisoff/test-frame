from src.web.locator import Locator
from src.web.pages.auth.auth_page import AuthPage


class LoginPage(AuthPage):

    URL = f'{AuthPage.URL}/login'

    EMAIL_INPUT = Locator(
        name='поле для ввода email',
        locator="//input[@id='auth_email']"
    )
    PASSWORD_INPUT = Locator(
        name='поле для ввода email',
        locator="//input[@id='auth_email']"
    )
    LOGIN_TEXT = Locator(
        name='заголовок с текстом "Вход в Умскул"',
        locator="//h2[contains(text(), 'Вход в Умскул')]"
    )
    FORGOT_PASSWORD_LINK = Locator(
        name='ссылка на страницу восстановления пароля',
        locator="//a[contains(text(), 'Забыли пароль')]"
    )
    SING_IN_LINK = Locator(
        name='ссылка на форму регистрации',
        locator="//a[contains(text(), 'Зарегистрироваться')]"
    )
    CONTACT_PHONE = Locator(
        name='номер поддержки',
        locator="//span[contains(text(), '8 800 300 63 24')]"
    )
    CONTACT_PHONE_LINK = Locator(
        name='ссылка на номер поддержки',
        locator="//a[contains(@href, 'tel:88003006324')]"
    )
    CONTACT_EMAIL = Locator(
        name='номер поддержки',
        locator="//span[contains(text(), 'support@umschool.ru')]"
    )
    CONTACT_EMAIL_LINK = Locator(
        name='ссылка на почту поддержки',
        locator="//a[contains(@href, 'mailto:support@umschool.r')]"
    )
    CONTACT_CHAT = Locator(
        name='номер поддержки',
        locator="//a[contains(@href, 'https://vk.me/umschoolhelp')]"
    )

    def open_current_page(self):
        print('234567')
        self.open_page(self.URL)

    def check_base_elements_visibility(self):
        """ Проверка отображения базовых элементов на станице https://nd.umschool.net/auth/login """

        self.find_visible_element(self.LOGIN_TEXT)
        self.find_visible_element(self.EMAIL_INPUT)
        self.find_visible_element(self.PASSWORD_INPUT)
        self.find_visible_element(self.FORGOT_PASSWORD_LINK)
        self.find_visible_element(self.SING_IN_LINK)
        self.find_visible_element(self.CONTACT_CHAT)
        self.find_visible_element(self.CONTACT_PHONE)
        self.find_visible_element(self.CONTACT_PHONE_LINK)
        self.find_visible_element(self.CONTACT_EMAIL)
        self.find_visible_element(self.CONTACT_EMAIL_LINK)
