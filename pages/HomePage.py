from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

DROPDOWN_MENU = (By.ID, "com.leavjenn.hews:id/iv_expander")
LOGIN_BUTTON = (By.ID, "com.leavjenn.hews:id/design_menu_item_text")
LOGGED_USER_LABEL = (By.ID, "com.leavjenn.hews:id/tv_account")
MAGNIFIER_BUTTON = (By.ID, "com.leavjenn.hews:id/action_search")


class HomePage(BasePage):
    def open_burger_menu(self):
        super().find_element(ec.visibility_of_element_located(MAGNIFIER_BUTTON))
        self.driver.swipe(0, 100, 500, 100)

    def open_login_screen(self):
        self.open_burger_menu()
        super().find_element(ec.visibility_of_element_located(DROPDOWN_MENU)).click()
        super().find_element(ec.visibility_of_element_located(LOGIN_BUTTON)).click()

    def get_logged_user(self):
        self.open_burger_menu()
        return super().find_element(ec.visibility_of_element_located(LOGGED_USER_LABEL)).get_attribute("text")
