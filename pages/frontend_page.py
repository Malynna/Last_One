from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Frontend_helper:

    def __init__(self, app):
        self.app = app

    def check_search_products(self):
        wd = self.app.wd
        return wd.find_element_by_name("query")

    def go_to_category(self, category_name):
        wd = self.app.wd
        wd.find_element_by_class_name("%s" % category_name).click()

    def check_label_new_on_product(self, product_name):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@alt = '%s']/../*[@title = 'New']" % product_name)

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

    def fill_in_personal_fields(self, tax_id, company, first_name, last_name, address_1, address_2,
                                postal_code, city, email, phone):
        wd = self.app.wd
        wait = self.app.common.wait()
        tax_id_box = wait.until(EC.visibility_of_element_located((By.NAME,("tax_id"))))
        tax_id_box.click()
        tax_id_box.clear()
        tax_id_box.send_keys(tax_id)
        company_box = wd.find_element_by_name("company")
        company_box.click()
        company_box.clear()
        company_box.send_keys(company)
        first_name_box = wd.find_element_by_name("firstname")
        first_name_box.click()
        first_name_box.clear()
        first_name_box.send_keys(first_name)
        last_name_box = wd.find_element_by_name("lastname")
        last_name_box.click()
        last_name_box.clear()
        last_name_box.send_keys(last_name)
        address_1_box = wd.find_element_by_name("address1")
        address_1_box.click()
        address_1_box.clear()
        address_1_box.send_keys(address_1)
        address_2_box = wd.find_element_by_name("address2")
        address_2_box.click()
        address_2_box.clear()
        address_2_box.send_keys(address_2)
        postal_code_box = wd.find_element_by_name("postcode")
        postal_code_box.click()
        postal_code_box.clear()
        postal_code_box.send_keys(postal_code)
        city_box = wd.find_element_by_name("city")
        city_box.click()
        city_box.clear()
        city_box.send_keys(city)
        email_box = wd.find_element_by_name("email")
        email_box.click()
        email_box.clear()
        email_box.send_keys(email)
        phone_box = wd.find_element_by_name("phone")
        phone_box.click()
        phone_box.clear()
        phone_box.send_keys(phone)

    def click_button_save_changes(self):
        wait = self.app.common.wait()
        wait.until(EC.element_to_be_clickable((By.NAME, "save_customer_details"))).click()

    def click_button_confirm_order(self):
        wait = self.app.common.wait()
        wait.until(EC.element_to_be_clickable((By.NAME, "confirm_order"))).click()

    def fill_fields_and_confirm_order(self, tax_id, company, first_name, last_name, address_1, address_2,
                                      postal_code, city, email, phone):
        self.fill_in_personal_fields(tax_id, company, first_name, last_name, address_1, address_2,
                                     postal_code, city, email, phone)
        self.click_button_save_changes()
        self.click_button_confirm_order()