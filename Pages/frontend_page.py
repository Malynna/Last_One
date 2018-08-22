from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class frontend_helper:

    def __init__(self, app):
        self.app = app

    def go_to_category(self):
        wd = self.app.wd
        wd.find_element_by_class_name("category-3").click()

    def check_label_new_on_product(self, product_name):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "//*[@alt = '%s']/../*[@title = 'New']" % product_name)

    def check_url(self, url):
        return EC.url_contains(url)

    def check_shopping_cart(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.title")

