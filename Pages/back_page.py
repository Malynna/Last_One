from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
from random import *
from selenium.webdriver.support.ui import Select


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

    def add_new_product_button(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Add New Product')]"))).click()

    def set_enable_status_in_new_product(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label.btn.btn-default").click()

    def set_category_in_checkbox(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='categories[]' and @data-name='Root']").click()
        check_root = wd.find_element_by_xpath("//input[@name='categories[]' and @data-name='Root']").is_selected()
        if check_root:
            wd.find_element_by_xpath("//input[@name='categories[]' and @data-name='Root']").click()
            print ('Checkbox Root is not selected now')
        else:
            print ('Checkbox Root is unselected')

        check = wd.find_element_by_xpath("//input[@name='categories[]' and @data-name='Łukasz']").is_selected()
        if check:
            print ('Checkbox Łukasz is already selected')
        else:
            wd.find_element_by_xpath("//input[@name='categories[]' and @data-name='Łukasz']").click()
            print ('Checkbox Łukasz is selected now')

    def random_chars(self, min_chars, max_chars):
        allchars = string.ascii_letters + string.digits
        return "".join(choice(allchars) for x in range(randint(min_chars, max_chars)))

    def random_price(self, min_chars, max_chars):
        return "".join(choice(string.digits) for x in range (randint(min_chars, max_chars)))

    def set_name_of_new_product(self,product_name):
        wd = self.app.wd
        name_box = wd.find_element_by_name("name[en]")
        name_box.click()
        name_box.send_keys(product_name)

    #def set_code_of_new_product(self,product_code):
    #    wd = self.app.wd
    #    name_box = wd.find_element_by_name("code")
    #    name_box.click()
    #    name_box.send_keys(product_code)

    def go_to_new_product_price_tab(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'Prices')]").click()

    def set_USD_price(self, price):
        wd = self.app.wd
        USD_price = wd.find_element_by_name("gross_prices[USD]")
        USD_price.click()
        USD_price.send_keys(price)

    def go_to_new_product_stock_tab(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'Stock')]").click()

    def set_backorder_item(self):
        wd = self.app.wd
        select = Select(wd.find_element_by_name("sold_out_status_id"))
        select.select_by_visible_text('Backorder Item')

    def save_new_product(self):
        wd = self.app.wd
        wd.find_element_by_name("save").click()

    def go_to_front_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("i.fa.fa-chevron-circle-left").click()



