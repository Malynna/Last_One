from selenium import webdriver
from Pages.backend_page import backend_helper
from Pages.common import commmon_helper
from Pages.frontend_page import frontend_helper

class application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.back = backend_helper(self)
        self.front = frontend_helper(self)
        self.common = commmon_helper(self)

    def open_url(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()