
from src.web.locator import Locator

class MainPageLocators():
    SEARCH_INPUT = Locator(
        name='поле посика',
        locator='//input[@id="a11y-search-input"]'
    )
    FIND_WORK_BUTTON = Locator(
        name='кнопка "Найти работу"',
        locator="//span[contains(text(), 'Найти работу')]"
    )
    ADVANCED_SEARCH_BUTTON = Locator(
        name='кнопка "Расширенный поиск"',
        locator="/a[contains(@data-qa, 'advanced-search')]",
    )
    FOR_COMPANIES_LINK = Locator(
        name='ссылка "Работодателям"',
        locator='//a[contains(@data-qa, "mainmenu_employer")]'
    )
    FOR_EMPLOYERS_LINK = Locator(
        name='ссылка "Соискателям"',
        locator='//a[contains(@data-qa, "mainmenu_applicant")]'
    )
    ALL_SERVICES_BUTTON = Locator(
        name='кнопка "Все сервисы"',
        locator='//span[contains(text(), "Все сервисы")]'
    )
    SING_IN_BUTTON = Locator(
        name='кнопка "Войти"',
        locator='//a[contains(text(), "Войти")]'
    )

