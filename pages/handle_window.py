import time
from win32com import client
import win32com
from config import config

def Handle_window(self):
    wd = self.wd
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Sendkeys(config.username)
    time.sleep(2)
    shell.Sendkeys("{TAB}")
    time.sleep(2)
    shell.Sendkeys(config.password)
    time.sleep(2)
    shell.Sendkeys("{ENTER}")
    time.sleep(2)