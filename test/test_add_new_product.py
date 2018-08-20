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
    app.open_url(config.admin_url)
    assert app.session.check_tittle() == "OSTATECZNE ZADANIE"
    app.back.set_username(config.username)
    app.back.set_password(config.password)
    app.back.login()
    app.back.go_to_catalog()
    app.back.add_new_product_button()
