from src.web.base_page import BasePage, BaseRoute

class AuthPage(BasePage):
    " Начальный класс для страниц авторизации "

    URL = f'{BaseRoute.BASE_URL}auth'


