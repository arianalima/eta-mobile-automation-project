from pages.BasePage import BasePage
from utils import constants
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

USERNAME_LABEL = (By.ID, "com.leavjenn.hews:id/tilayout_user_name")
USERNAME_INPUT = (By.ID, "com.leavjenn.hews:id/et_user_name")
PASSWORD_LABEL = (By.ID, "com.leavjenn.hews:id/tilayout_password")
PASSWORD_INPUT = (By.ID, "com.leavjenn.hews:id/et_password")
CANCEL_BUTTON = (By.ID, "android:id/button2")
LOGIN_BUTTON = (By.ID, "android:id/button1")
WARN_MESSAGE = (By.ID, "com.leavjenn.hews:id/tv_prompt")
POPUP_TITLE = (By.ID, "android:id/alertTitle")


class LoginPage(BasePage):
    def confirm_login(self):
        login_button = super().find_element(ec.visibility_of_element_located(LOGIN_BUTTON))
        login_button.click()

    def cancel_login(self):
        super().find_element(ec.visibility_of_element_located(CANCEL_BUTTON)).click()

    def insert_username(self, username):
        super().find_element(ec.visibility_of_element_located(USERNAME_INPUT)).send_keys(username)

    def insert_password(self, password):
        super().find_element(ec.visibility_of_element_located(PASSWORD_INPUT)).send_keys(password)

    def check_username_label(self):
        return super().find_element(ec.visibility_of_element_located(USERNAME_LABEL)).get_attribute("text") == constants.USERNAME_LABEL

    def check_password_label(self):
        return super().find_element(ec.visibility_of_element_located(PASSWORD_LABEL)).get_attribute("text") == constants.PASSWORD_LABEL

    def check_cancel_button_label(self):
        return super().find_element(ec.visibility_of_element_located(CANCEL_BUTTON)).get_attribute("text") == constants.CANCEL_LABEL

    def check_login_button_label(self):
        return super().find_element(ec.visibility_of_element_located(LOGIN_BUTTON)).get_attribute("text") == constants.LOGIN_LABEL

    def get_warn_message(self):
        return super().find_element(ec.visibility_of_element_located(WARN_MESSAGE)).get_attribute("text")

    def check_title_message(self):
        return super().find_element(ec.visibility_of_element_located(POPUP_TITLE)).get_attribute("text") == constants.POPUP_TITLE

    def check_title_invisibility(self):
        return super().find_element(ec.invisibility_of_element(POPUP_TITLE))
