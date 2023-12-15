import pytest

@pytest.fixture
def open_page(request):
    page = request.node.get_closest_marker("open_page").args[0]
    page.open_current_page()

    return page

