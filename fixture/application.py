from selenium import webdriver
from fixture.session import SessionHelper
from config import config

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_home_page(self, url):
        wd = self.wd
        wd.get(url)

    def destroy(self):
        self.wd.quit()