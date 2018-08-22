import pytest
from fixture.application import application
from config import config




@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_product(app):
    product_name = "P " + app.back.random_chars(5, 8)
    price = app.back.random_price(1,3)
    app.open_url(config.admin_url)
    assert app.common.check_tittle() == "OSTATECZNE ZADANIE"
    app.back.login(config.username, config.password)
    assert app.back.check_logout()

    app.back.go_to_front_page()
    assert app.front.check_url(config.base_url)
    app.front.go_to_category()
    assert app.front.check_label_new_on_product(product_name)