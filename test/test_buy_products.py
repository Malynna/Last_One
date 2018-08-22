import pytest
from fixture.application import application
from config import config
import time


@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_products(app):
    app.open_url(config.base_url)
    assert app.front.check_url(config.base_url)
    app.front.go_to_category_XiaomiLepsze()
    assert app.front.check_category()
    app.front.click_product(config.first_product)
    app.front.add_product_to_cart()
    time.sleep(1)