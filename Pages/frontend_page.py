from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import config

class frontend_helper:

    def __init__(self, app):
        self.app = app

    def go_to_category_Lukasz(self):
        wd = self.app.wd
        wd.find_element_by_class_name("category-3").click()

    def go_to_category_XiaomiLepsze(self):
        wd = self.app.wd
        wd.find_element_by_class_name("category-1").click()

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

    def click_button_add_to_cart(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector(".btn-success").click()


