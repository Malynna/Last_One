


class front_helper:

    def __init__(self, app):
        self.app = app

    def go_to_category(self):
        wd = self.app.wd
        wd.find_element_by_class_name("category-3").click()

    def find_already_added_product(self, product_name):
        wd = self.app.wd
        products = wd.find_elements_by_class_name("name")
        for e in products:
            if e.text == product_name:
                print(product_name)
                break