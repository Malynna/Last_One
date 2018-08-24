from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class frontend_helper:

    def __init__(self, app):
        self.app = app

    def go_to_category(self, category_name):
        wd = self.app.wd
        wd.find_element_by_class_name("%s" % category_name).click()

    def check_label_new_on_product(self, product_name):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@alt = '%s']/../*[@title = 'New']" % product_name)

    def check_url(self, url):
        return EC.url_contains(url)

    def check_shopping_cart(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.title").text == "Shopping Cart"

    def check_category(self):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//h1[@class = 'title']").text == "XiaomiLepsze"

    def click_product(self, product_name):
        wd = self.app.wd
        return wd.find_element_by_css_selector(".product.column.hover-light[data-name='%s']" % product_name).click()

    def max_window(self):
        wait = self.app.common.wait()
        wait.until(EC.visibility_of_element_located((By.ID, "view-full-page"))).click()

    def check_number_of_producs_in_cart(self):
        wd = self.app.wd
        products = int(wd.find_element_by_css_selector("div#cart span.quantity").text)
        return products

    def check_no_emptyness_in_cart(self):
        if self.check_number_of_producs_in_cart() >0: return True

    def click_button_add_to_cart(self):
        products = self.check_number_of_producs_in_cart()
        wait = self.app.common.wait()
        wd = self.app.wd
        wait.until(EC.visibility_of_element_located((By.NAME, "add_cart_product"))).click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div#cart span.quantity"), str(products + 1)))

    def add_product_to_cart(self, product_name, category_name):
        wd = self.app.wd
        self.go_to_category(category_name)
        self.click_product(product_name)
        self.max_window()
        self.click_button_add_to_cart()

    def go_to_cart(self):
        wd = self.app.wd
        return wd.find_element_by_id("cart").click()

    def fill_in_personal_fields(self):
        wd = self.app.wd
        tax_id_box = wd.find_element_by_name("tax_id")
        tax_id_box.click()
        tax_id_box.clear()
        tax_id_box.send_keys(tax_id)
        company_box = wd.find_element_by_name("tax_id")
        company_box.click()
        company_box.clear()
        company_box.send_keys(tax_id)
        first_name_box = wd.find_element_by_name("tax_id")
        first_name_box.click()
        first_name_box.clear()
        first_name_box.send_keys(tax_id)
        last_name_box = wd.find_element_by_name("tax_id")
        last_name_box.click()
        last_name_box.clear()
        last_name_box.send_keys(tax_id)
        address_1_box = wd.find_element_by_name("tax_id")
        address_1_box.click()
        address_1_box.clear()
        address_1_box.send_keys(tax_id)
        address_2_box = wd.find_element_by_name("tax_id")
        address_2_box.click()
        address_2_box.clear()
        address_2_box.send_keys(tax_id)
        postal_code_box = wd.find_element_by_name("tax_id")
        postal_code_box.click()
        postal_code_box.clear()
        postal_code_box.send_keys(tax_id)
        city_box = wd.find_element_by_name("tax_id")
        city_box.click()
        city_box.clear()
        city_box.send_keys(tax_id)
        email_box = wd.find_element_by_name("tax_id")
        email_box.click()
        email_box.clear()
        email_box.send_keys(tax_id)
        phone_box = wd.find_element_by_name("tax_id")
        phone_box.click()
        phone_box.clear()
        phone_box.send_keys(tax_id)