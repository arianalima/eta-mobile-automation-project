from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utils.constants import POPUP_TITLE

DROPDOWN_MENU = (By.ID, "com.leavjenn.hews:id/iv_expander")
LOGIN_BUTTON = (By.ID, "com.leavjenn.hews:id/design_menu_item_text")
LOGOUT_BUTTON = (By.ID, "com.leavjenn.hews:id/design_menu_item_text")


class HomePage(BasePage):
    def open_burger_menu(self):
        self.driver.swipe(0, 100, 500, 100)

    def open_login_screen(self):
        self.open_burger_menu()
        super().find_element(ec.visibility_of_element_located(DROPDOWN_MENU)).click()
        super().find_element(ec.visibility_of_element_located(LOGIN_BUTTON)).click()

    def logout(self):
        self.open_burger_menu()
        super().find_element(ec.visibility_of_element_located(DROPDOWN_MENU)).click()
        super().find_element(ec.visibility_of_element_located(LOGOUT_BUTTON)).click()

    def check_login_button(self):
        self.open_burger_menu()
        super().find_element(ec.visibility_of_element_located(DROPDOWN_MENU)).click()
        return super().find_element(ec.visibility_of_element_located(LOGIN_BUTTON)).get_attribute("text") == POPUP_TITLE
