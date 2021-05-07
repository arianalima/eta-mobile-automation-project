import os
import unittest
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumCurso(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'app': os.path.join(os.path.dirname(__file__), 'utils', "Hews.apk"),
            'newCommandTimeout': 10000
        }

        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        time.sleep(3)

    def tearDown(self):
        # self.instance.quit()
        pass

    def test_01(self):
        print("alo")

    def test_open_login(self):
        self.instance.swipe(0, 100, 500, 100)
        dropdown_button = self.instance.find_element_by_id("com.leavjenn.hews:id/iv_expander").click()
        login_button = self.instance.find_element_by_id("com.leavjenn.hews:id/design_menu_item_text").click()
        time.sleep(1)

        # username_label = self.instance.find_element_by_id("com.leavjenn.hews:id/tilayout_user_name").get_attribute("text")
        # password_label = self.instance.find_element_by_id("com.leavjenn.hews:id/tilayout_password").get_attribute("text")
        # username_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        # password_input = self.instance.find_element_by_id("com.leavjenn.hews:id / et_password")
        # cancel_button = self.instance.find_element_by_id("android:id / button2")
        # login_button = self.instance.find_element_by_id("android:id / button1")
        # warn_message = self.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        # popup_title = self.instance.find_element_by_id("android:id/alertTitle")
