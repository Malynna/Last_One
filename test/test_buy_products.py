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
    app.front.go_to_category(app.vars.cat_XiaomiLepsze)
    assert app.front.check_category()
    app.front.add_product_to_cart(app.vars.first, app.vars.cat_XiaomiLepsze)
    app.front.add_product_to_cart(app.vars.second, app.vars.cat_XiaomiLepsze)
    app.front.add_product_to_cart(app.vars.third, app.vars.cat_XiaomiLepsze)
    app.front.go_to_cart()