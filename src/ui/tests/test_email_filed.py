import pytest
from src.ui.pages.yandex_passport_form import YandexPassportForm
from src.geterators.random_string import generate_random_string
from .constants import ERROR_MESSAGE
class TestEmailField():

    @pytest.mark.smok
    @pytest.mark.open_page(YandexPassportForm())
    def test_email_input_incorrect_mail(self, open_page, get_test_user):
        current_page = open_page
        email = get_test_user['email'].lower()
        assert current_page.enter_email(email), ERROR_MESSAGE

    @pytest.mark.smok
    @pytest.mark.open_page(YandexPassportForm())
    def test_email_input_with_random_symbols(self, open_page, get_test_user):
        current_page = open_page
        assert current_page.enter_email(generate_random_string(10)), ERROR_MESSAGE

    @pytest.mark.smok
    @pytest.mark.open_page(YandexPassportForm())
    def test_email_input_empty_enter(self, open_page, get_test_user):
        current_page = open_page
        assert current_page.enter_email(''), ERROR_MESSAGE








