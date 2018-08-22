from selenium.webdriver.support.wait import WebDriverWait


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