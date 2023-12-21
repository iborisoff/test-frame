import pytest
from src.ui.pages.yandex_passport_form import YandexPassportForm

from .constants import ERROR_MESSAGE


class TestPhoneFiled:

    @pytest.mark.smok
    @pytest.mark.open_page(YandexPassportForm())
    def test_phone_input_with_empty_number(self, open_page, get_test_user):
        current_page = open_page
        assert current_page.enter_phone_number(), ERROR_MESSAGE

    @pytest.mark.smok
    @pytest.mark.open_page(YandexPassportForm())
    def test_phone_input_with_wrong_number(self, open_page, get_test_user):
        current_page = open_page
        phone = get_test_user['phone']
        assert current_page.enter_phone_number(phone), ERROR_MESSAGE
