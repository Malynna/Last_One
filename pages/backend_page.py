__author__= "Malinex"
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BackendHelper:

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

    def login_button(self):
        wd = self.app.wd
        wait = self.app.common.wait()
        wd.find_element_by_class_name("btn").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@title = 'Logout']")))

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.login_button()

    def go_to_catalog(self):
        wait = self.app.common.wait()
        wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Catalog"))).click()

    def set_category(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Łukasz").click()

    def new_product_button(self):
        wait = self.app.common.wait()
        return wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Add New Product")))

    def click_new_product_button(self):
        wait = self.app.common.wait()
        return wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Add New Product"))).click()

    def set_enable_status_in_product(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label.btn.btn-default").click()

    def set_name_of_product(self, product_name):
        wd = self.app.wd
        name_box = wd.find_element_by_name("name[en]")
        name_box.click()
        name_box.clear()
        name_box.send_keys(product_name)

    def go_to_product_price_tab(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Prices").click()

    def set_usd_price(self, price):
        wd = self.app.wd
        usd_price = wd.find_element_by_name("gross_prices[USD]")
        usd_price.click()
        usd_price.clear()
        usd_price.send_keys(price)

    def go_to_product_stock_tab(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Stock").click()

    def set_backorder_item(self):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("sold_out_status_id"))
        select.select_by_visible_text('Backorder Item')

    def save_product(self):
        wd = self.app.wd
        wd.find_element_by_name("save").click()

    def add_new_product(self,product_name,price):
        self.go_to_catalog()
        self.set_category()
        self.click_new_product_button()
        self.set_enable_status_in_product()
        self.set_name_of_product(product_name)
        self.go_to_product_price_tab()
        self.set_usd_price(price)
        self.go_to_product_stock_tab()
        self.set_backorder_item()
        self.save_product()
        self.new_product_button()

    def go_to_front_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("i.fa-chevron-circle-left").click()

    def check_logout(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@title = 'Logout']")
