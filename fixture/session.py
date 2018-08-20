


class session_helper:

    def __init__(self, app):
        self.app = app

    def check_tittle(self):
        wd = self.app.wd
        return wd.title