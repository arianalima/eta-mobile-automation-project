import os

from appium import webdriver


class DriverManager:
    def __init__(self):
        self.desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'app': os.path.join(os.path.dirname(__file__), "Hews.apk"),
            'newCommandTimeout': 10000
        }

    def connect_to_server(self):
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_cap)
        return self.instance

    def get_instance(self):
        return self.instance

    def disconnect_server(self):
        self.instance.quit()
