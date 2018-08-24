from selenium import webdriver
from pages.backend_page import Backend_helper
from pages.common import Commmon_helper
from pages.frontend_page import Frontend_helper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.back = Backend_helper(self)
        self.front = Frontend_helper(self)
        self.common = Commmon_helper(self)

    def open_url(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()