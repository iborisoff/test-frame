import pytest
import requests

class TestBookShop:
    URL='https://mockapi.io/projects/65647e24ceac41c0761e490e'
    @pytest.mark.api
    def test_books(self):
        response = requests.get(f'{self.URL}/books')
        assert response.status_code == 200, 'Ooops'

    @pytest.mark.api
    def test_books(self):
        response = requests.get(f'{self.URL}/reads')
        assert response.status_code == 200, 'Ooops'

