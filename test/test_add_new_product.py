import pytest
from fixture.application import Application
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from config import config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    wd = app.wd
    app.open_home_page(config.admin_url)
    alert = wd.switch_to_alert()
    alert.send_keys("asdads")
    alert.accept()
    time.sleep(8)
    wd.find_element_by_name("cusid").click()