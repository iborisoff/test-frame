from src.core.selenium import Locator

from .main_page import MainPage


class HeaderElements(MainPage):
    SEARCH_INPUT = Locator(
        name='поле поиска товаров',
        locator="//input[@placeholder='Искать на Ozon']"
    )
    SEARCH_BUTTON = Locator(
        name='кнопка "Искать"',
        locator="//button[@type='submit' and @aria-label='Поиск']"
    )
    MENU_BUTTON = Locator(
        name='кнопка "Каталог"',
        locator="//div[contains(text(), 'Каталог')]"
    )
    LOGIN_BUTTON = Locator(
        name='кнопка "Войти"',
        locator="//div[@data-widget='profileMenuAnonymous']"
    )
    ORDER_LIST_BUTTON = Locator(
        name='кнопка "Список заказов"',
        locator="//a[@href='/my/orderlist']",
    )
    MY_FAVORITES_BUTTON = Locator(
        name='кнопка "Понравивщиеся товары"',
        locator="//a[@href='/my/favorites']",
    )
    CART_BUTTON = Locator(
        name='кнопка "Корзина"',
        locator="//a[@href='/cart']",
    )
    OZON_FRESH_LINK = Locator(
        name='Ozon fresh',
        locator="//a[contains(text(), 'Ozon fresh')]"
    )
    OZON_CARD_LINK = Locator(
        name='Ozon Карта',
        locator="//a[contains(text(), 'Ozon Карта')]"
    )
    BOOKING_LINK = Locator(
        name='Билеты, отели, туры',
        locator="//a[contains(text(), 'Билеты, отели, туры')]"
    )
    CLOTH_LINK = Locator(
        name='Одежда и обувь',
        locator="//a[contains(text(), 'Одежда и обувь')]"
    )
    ELECTRONIC_LINK = Locator(
        name='Электроника',
        locator="//a[contains(text(), 'Электроника')]"
    )
    HOME_GARDEN_LINK = Locator(
        name='Дом и сад',
        locator="//a[contains(text(), 'Дом и сад')]"
    )
    CHILDENS_GOODS_LINK = Locator(
        name='Детские товары',
        locator="//a[contains(text(), 'Детские товары')]"
    )
    ACTIONS_LINK = Locator(
        name='Акции',
        locator="//a[contains(text(), 'Акции')]"
    )
    PREMIUM_LINK = Locator(
        name='Premium',
        locator="//a[contains(text(), 'Premium')]"
    )

    def open_current_page(self):
        self.open_page(self.URL)

    def check_elements_visibility(self):
        self.find_visible_element(self.SEARCH_INPUT)
        self.find_visible_element(self.SEARCH_BUTTON)
        self.find_visible_element(self.MENU_BUTTON)
        self.find_visible_element(self.PREMIUM_LINK)
        self.find_visible_element(self.ACTIONS_LINK)
        self.find_visible_element(self.CHILDENS_GOODS_LINK)
        self.find_visible_element(self.HOME_GARDEN_LINK)
        self.find_visible_element(self.ELECTRONIC_LINK)
        self.find_visible_element(self.CLOTH_LINK)
        self.find_visible_element(self.BOOKING_LINK)
        self.find_visible_element(self.OZON_CARD_LINK)
        self.find_visible_element(self.OZON_FRESH_LINK)
        self.find_visible_element(self.ORDER_LIST_BUTTON)
        self.find_visible_element(self.MY_FAVORITES_BUTTON)
        self.find_visible_element(self.LOGIN_BUTTON)
        self.find_visible_element(self.CART_BUTTON)
        return True

    def open_cart_page(self):
        self.click_on_element(self.CART_BUTTON)
        return self.current_url

    def open_order_list_page(self):
        self.click_on_element(self.ORDER_LIST_BUTTON)
        return self.current_url

    def open_ozon_card_page(self):
        self.click_on_element(self.OZON_CARD_LINK)
        return self.current_url

    def open_favorites_page(self):
        self.click_on_element(self.MY_FAVORITES_BUTTON)
        return self.current_url

    def open_travel_page(self):
        self.click_on_element(self.BOOKING_LINK)
        return self.current_url

    def open_cloth_page(self):
        self.click_on_element(self.CLOTH_LINK)
        return self.current_url

    def open_electronic_page(self):
        self.click_on_element(self.ELECTRONIC_LINK)
        return self.current_url

    def open_home_garden_page(self):
        self.click_on_element(self.HOME_GARDEN_LINK)
        return self.current_url

    def open_action_page(self):
        self.click_on_element(self.ACTIONS_LINK)
        return self.current_url

    def open_childens_goods_page(self):
        self.click_on_element(self.CHILDENS_GOODS_LINK)
        return self.current_url

    def open_premium_page(self):
        self.click_on_element(self.PREMIUM_LINK)
        return self.current_url
