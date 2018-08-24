from selenium import webdriver
from fixture.session import SessionHelper
from config import config

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)
