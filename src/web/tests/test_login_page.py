import pytest
from src.web.pages.auth.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.smock
class TestLoginPage:

    @pytest.mark.open_page(LoginPage())
    @pytest.mark.ui
    def test_elements_display(self, open_page: LoginPage):
        open_page.wait_timeout(float(20))
        assert open_page.check_base_elements_visibility(), \
            'Нет инпутов, ссылок на: поддержку, смену пароля, форму регистрации'

