from selenium import webdriver
from pages.backend_page import backend_helper
from pages.common import *
from pages.frontend_page import frontend_helper

class application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.back = backend_helper(self)
        self.front = frontend_helper(self)
        self.common = commmon_helper(self)
        self.vars = variables(self)

    def open_url(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()