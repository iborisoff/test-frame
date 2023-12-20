import pytest
from src.api.users import JsonplaPceholderUsers
@pytest.fixture
def open_page(request):
    page = request.node.get_closest_marker("open_page").args[0]
    page.open_current_page()

    return page
@pytest.fixture
def get_test_user():
    users = JsonplaPceholderUsers()
    return users.firstUser
