import pytest
from fixture.application import application
from config import config
from data.test_data import test_data as td
import time

@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_product(app):

    app.open_url(config.admin_url)
    assert app.common.check_tittle() == "OSTATECZNE ZADANIE"
    app.back.login(config.username, config.password)
    assert app.back.check_logout()
    app.back.add_new_product(td.product_name, td.price)
    app.back.go_to_front_page()
    assert app.front.check_shopping_cart()
    app.front.go_to_category(td.categories["Lukasz"])
    assert app.front.check_label_new_on_product(td.product_name)