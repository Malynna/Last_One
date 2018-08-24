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
    app.front.add_product_to_cart(td.products["first"], td.categories["phones"])
    app.front.add_product_to_cart(td.products["second"], td.categories["phones"])
    app.front.add_product_to_cart(td.products["third"], td.categories["phones"])
    app.front.go_to_cart()
    app.front.fill_in_personal_fields(td.products["tax_id"], td.products["company"], td.products["first_name"],
                                      td.products["last_name"], td.products["address_1"], td.products["address_2"],
                                      td.products["postal_code"], td.products["city"], td.products["email"],
                                      td.products["phone"])