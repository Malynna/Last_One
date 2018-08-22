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
    app.front.go_to_category(config.category_XiaomiLepsze)
    assert app.front.check_category()
    app.front.add_product_to_cart(config.first_product,config.category_XiaomiLepsze)
    time.sleep(30)
    app.front.add_product_to_cart(config.second_product,config.category_XiaomiLepsze)
    app.front.add_product_to_cart(config.third_product,config.category_XiaomiLepsze)
    app.front.go_to_cart()
    time.sleep(5)