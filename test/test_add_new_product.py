import pytest
from fixture.application import application
from config import config

@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_product(app):

    price = app.common.random_digits(1, 3)
    product_name = "P " + app.common.random_chars(5, 8)
    app.open_url(config.admin_url)
    assert app.common.check_tittle() == "OSTATECZNE ZADANIE"
    app.back.login(config.username, config.password)
    assert app.back.check_logout()
    app.back.add_new_product(product_name,price)
    app.back.go_to_front_page()
    assert app.front.check_shopping_cart()
    app.front.go_to_category(app.vars.cat_Lukasz)
    assert app.front.check_label_new_on_product(product_name)