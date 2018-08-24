import pytest
from fixture.application import application
from config import config
from data.test_data import test_data as td


@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_products(app):
    app.open_url(config.base_url)
    assert app.front.check_url(config.base_url)
    app.front.go_to_category(td.categories["XiaomiLepsze"])
    assert app.front.check_category()
    app.front.add_product_to_cart(td.products["first"], td.categories["XiaomiLepsze"])
    app.front.add_product_to_cart(td.products["second"], td.categories["XiaomiLepsze"])
    app.front.add_product_to_cart(td.products["third"], td.categories["XiaomiLepsze"])
    app.front.go_to_cart()