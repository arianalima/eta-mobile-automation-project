import os
import sys

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from behave import step


PARENT_PATH = os.path.abspath("../..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


@step('I access the app')
def open_app(context):
    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)
