from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class back_helper:

    def __init__(self, app):
        self.app = app

    def set_username(self, username):
        wd = self.app.wd
        username_box = wd.find_element_by_name("username")
        username_box.click()
        username_box.clear()
        username_box.send_keys(username)

    def set_password(self, password):
        wd = self.app.wd
        password_box = wd.find_element_by_name("password")
        password_box.click()
        password_box.clear()
        password_box.send_keys(password)

    def login(self):
        wd = self.app.wd
        wd.find_element_by_class_name("btn").click()

    def go_to_catalog(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Catalog"))).click()