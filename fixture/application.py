from selenium import webdriver
from pages.backend_page import BackendHelper
from pages.common import CommmonHelper
from pages.frontend_page import FrontendHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.back = BackendHelper(self)
        self.front = FrontendHelper(self)
        self.common = CommmonHelper(self)

    def open_url(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()