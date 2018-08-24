import pytest
from fixture.application import Application
from config import config
from data.test_data import TestData as td

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_product(app):

    app.open_url(config.admin_url)
    assert app.common.check_tittle() == "OSTATECZNE ZADANIE"
    app.back.login(config.username, config.password)
    assert app.back.check_logout()
    app.back.add_new_product(td.products["new_product"], td.price)
    app.back.go_to_front_page()
    assert app.front.check_shopping_cart()
    app.front.go_to_category(td.categories["lukasz"])
    assert app.front.check_label_new_on_product(td.products["new_product"])
    app.front.add_product_to_cart(td.products["new_product"], td.categories["lukasz"])
    assert app.front.check_no_emptyness_in_cart()