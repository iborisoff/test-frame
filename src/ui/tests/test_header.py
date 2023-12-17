import pytest

from src.ui.pages.main_page.headers_elements import HeaderElements
from src.navigations.urls import URLS
@pytest.mark.ui
class TestHeadersElements:


    @pytest.mark.open_page(HeaderElements())
    def test_elements_visibility(self, open_page):
        assert open_page.check_elements_visibility() == True, 'Не удалось найти ссылки, кнопки или инпут в header страницы'


    @pytest.mark.open_page(HeaderElements())
    @pytest.mark.navigation
    def test_cart_links(self, open_page):
         assert open_page.open_cart_page() == URLS.CART


    @pytest.mark.open_page(HeaderElements())
    @pytest.mark.navigation
    def test_order_list_link(self, open_page):
        assert open_page.open_order_list_page() == URLS.ORDERS_LIST


    @pytest.mark.open_page(HeaderElements())
    @pytest.mark.navigation
    def test_ozon_card_link(self, open_page):
        assert open_page.open_ozon_card_page() == URLS.OZON_CARD




