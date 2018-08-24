import pytest
from fixture.application import Application
from config import config
from data.test_data import Test_data as td
import time

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_products(app):
    app.open_url(config.base_url)
    assert app.front.check_search_products()
    app.front.add_product_to_cart(td.products["first"], td.categories["phones"])
    app.front.add_product_to_cart(td.products["second"], td.categories["phones"])
    app.front.add_product_to_cart(td.products["third"], td.categories["phones"])
    app.front.go_to_cart()
    app.front.fill_fields_and_confirm_order(td.personal_data["tax_id"], td.personal_data["company"],
                                            td.personal_data["first_name"],td.personal_data["last_name"],
                                            td.personal_data["address_1"],td.personal_data["address_2"],
                                            td.personal_data["postal_code"], td.personal_data["city"],
                                            td.personal_data["email"],td.personal_data["phone"])
    assert app.front.check_message_on_site()