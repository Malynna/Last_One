import pytest
from fixture.application import application
from config import config



@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_products(app):
    app.open_url(config.base_url)
    assert app.front.check_url(config.base_url)
