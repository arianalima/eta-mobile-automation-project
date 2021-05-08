import os
import unittest
from appium import webdriver
import time


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
        self.open_login()

    def tearDown(self):
        self.instance.quit()

    def test_01_verify_login_fields(self):
        popup_title = self.instance.find_element_by_id("android:id/alertTitle")
        username_label = self.instance.find_element_by_id("com.leavjenn.hews:id/tilayout_user_name")
        username_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        password_label = self.instance.find_element_by_id("com.leavjenn.hews:id/tilayout_password")
        password_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        warn_message = self.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        cancel_button = self.instance.find_element_by_id("android:id/button2")
        login_button = self.instance.find_element_by_id("android:id/button1")
        assert popup_title.get_attribute("text"), "Login"
        assert username_label.get_attribute("text"), "Username"
        assert username_input.is_displayed()
        assert password_label.get_attribute("text"), "Password"
        assert password_input.is_displayed()
        assert warn_message.get_attribute("text"), "* Your password will NOT be saved"
        assert cancel_button.get_attribute("text"), "CANCEL"
        assert login_button.get_attribute("text"), "LOGIN"

    def test_02_invalid_user(self):
        username_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        password_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        login_button = self.instance.find_element_by_id("android:id/button1")
        username_input.send_keys("dummy")
        password_input.send_keys("dummy123")
        login_button.click()
        time.sleep(1)
        error_message = self.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt").get_attribute("text")
        assert error_message, "Arrr…wrong username/password"
        username_input.clear()
        password_input.clear()

    def test_03_short_password(self):
        username_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        password_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        login_button = self.instance.find_element_by_id("android:id/button1")
        username_input.send_keys("dummy")
        password_input.send_keys("dummy")
        login_button.click()
        time.sleep(1)
        error_message = self.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt").get_attribute("text")
        assert error_message, "You got a short…password"
        username_input.clear()
        password_input.clear()

    def test_04_empty_fields(self):
        username_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        password_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        login_button = self.instance.find_element_by_id("android:id/button1")
        login_button.click()
        time.sleep(1)
        username_input.send_keys("")
        password_input.send_keys("")
        error_message = self.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt").get_attribute("text")
        assert error_message, "Catch you, anonymous!"

    def test_05_cancel_login(self):
        cancel_button = self.instance.find_element_by_id("android:id/button2")
        cancel_button.click()
        search_button = self.instance.find_element_by_id("com.leavjenn.hews:id/action_search")
        assert search_button.is_displayed()

    def open_login(self):
        self.instance.swipe(0, 100, 500, 100)
        self.instance.find_element_by_id("com.leavjenn.hews:id/iv_expander").click()
        self.instance.find_element_by_id("com.leavjenn.hews:id/design_menu_item_text").click()
        time.sleep(1)
