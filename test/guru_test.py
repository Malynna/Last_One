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

def test_login_last_task(app):
    wd = app.wd
    app.open_home_page(config.guru_url)
    e = wd.find_element_by_name("cusid")
    e.click()
    e.send_keys("53920")
    wd.find_element_by_name("submit").click()
    alert = wd.switch_to_alert()
    alert.accept()
    alert.accept()
    time.sleep(8)
    wd.find_element_by_name("cusid").click()