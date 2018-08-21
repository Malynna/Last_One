from selenium import webdriver
from fixture.session import session_helper
from Pages.back_page import back_helper
from Pages.front_page import front_helper

class application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = session_helper(self)
        self.back = back_helper(self)
        self.front = front_helper(self)

    def open_url(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()