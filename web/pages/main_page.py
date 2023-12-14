from web.base_page import BasePage
from web.locators.main import MainPageLocators

class MainPage(BasePage):

    def is_page_open(self):
        self.find_visible_element(MainPageLocators.SEARCH_INPUT)
        self.find_visible_element(MainPageLocators.FIND_WORK_BUTTON)

    def open_main_page(self):
        self.open_page('https://kazan.hh.ru/')

