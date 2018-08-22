from selenium.webdriver.support.wait import WebDriverWait
import string
from random import *


class commmon_helper:

    def __init__(self, app):
        self.app = app

    def check_tittle(self):
        wd = self.app.wd
        return wd.title

    def wait(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5)
        return wait

    def random_chars(self, min_chars, max_chars):
        allchars = string.ascii_letters + string.digits
        return "".join(choice(allchars) for x in range(randint(min_chars, max_chars)))

    def random_digits(self, min_chars, max_chars):
        return "".join(choice(string.digits) for x in range(randint(min_chars, max_chars)))

class variables:

    cat_XiaomiLepsze = "category-1"
    cat_Lukasz = "category-3"
    first = "Mi A1"
    second = "Mi 8"
    third = "Mi Mix 2S"

    def __init__(self, app):
        self.app = app