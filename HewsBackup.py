import os
import unittest
from appium import webdriver
import time
import utils.DriverManager as dm
import pages.BasePage as bp

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumCurso(unittest.TestCase):
    def setUp(self):
        driver_manager = dm.DriverManager()
        driver_manager.connect_to_server()
        self.base_page = bp.BasePage()
        time.sleep(3)
        # self.open_login()

    def tearDown(self):
        # self.instance.quit()
        pass

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

    def test_02_invalid_fields(self):
        username_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        password_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_password")
        login_button = self.instance.find_element_by_id("android:id/button1")

    def test_open_login(self):
        self.base_page.swipe_to(0, 100, 500, 100)
        self.base_page.find_element("com.leavjenn.hews:id/iv_expander").click()
        self.base_page.find_element("com.leavjenn.hews:id/design_menu_item_text").click()
        time.sleep(1)

        # username_label = self.instance.find_element_by_id("com.leavjenn.hews:id/tilayout_user_name").get_attribute("text")
        # password_label = self.instance.find_element_by_id("com.leavjenn.hews:id/tilayout_password").get_attribute("text")
        # username_input = self.instance.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        # password_input = self.instance.find_element_by_id("com.leavjenn.hews:id / et_password")
        # cancel_button = self.instance.find_element_by_id("android:id / button2")
        # login_button = self.instance.find_element_by_id("android:id / button1")
        # warn_message = self.instance.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        # popup_title = self.instance.find_element_by_id("android:id/alertTitle")
