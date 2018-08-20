import pytest
from fixture.application import application
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from config import config

@pytest.fixture
def app(request):
    fixture = application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    wd = app.wd
    product_name = "New " + app.back.random_chars(3, 5)
#    product_code = "C" + app.back.random_chars(4, 7)
    price = app.back.random_price(1,3)
    app.open_url(config.admin_url)
    assert app.session.check_tittle() == "OSTATECZNE ZADANIE"
    app.back.set_username(config.username)
    app.back.set_password(config.password)
    app.back.login()
    app.back.go_to_catalog()
    app.back.add_new_product_button()
    app.back.set_enable_status_in_new_product()
    app.back.unset_root_category_in_checkbox()
    app.back.set_category_in_checkbox()
    app.back.set_name_of_new_product(product_name)
 #   app.back.set_code_of_new_product(product_code)
    app.back.go_to_new_product_price_tab()
    app.back.set_USD_price(price)
    app.back.go_to_new_product_stock_tab()
    app.back.set_backorder_item()
    time.sleep(2)
