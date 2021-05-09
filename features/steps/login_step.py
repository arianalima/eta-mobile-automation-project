import os
import subprocess
import sys
import time

from behave import step, then

from utils.constants import *
from utils.utils import get_messages_default

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


@step('I click on login page')
def click_on_login_page(context):
    context.home_page.open_login_screen()


@then('I should be able to see all fields displayed')
def verify_login_fields_displayed(context):
    assert context.login_page.check_title_message()
    assert context.login_page.check_username_label()
    assert context.login_page.check_password_label()
    assert context.login_page.check_warn_message()
    assert context.login_page.check_cancel_button_label()
    assert context.login_page.check_login_button_label()


@step('I insert a {user_type} user')
def insert_user(context, user_type):
    if user_type.lower() == "valid":
        context.login_page.insert_username(VALID_USERNAME)
    elif user_type.lower() == "invalid":
        context.login_page.insert_username(INVALID_USERNAME)


@step('I insert a {password_type} password')
def insert_password(context, password_type):
    if password_type.lower() == "valid":
        context.login_page.insert_password(VALID_PASSWORD_FOR_VALID_USERNAME)
    elif password_type.lower() == "invalid":
        context.login_page.insert_password(INVALID_PASSWORD)
    elif password_type.lower() == "short":
        context.login_page.insert_password(SHORT_PASSWORD)


@step('I select the {button_label} button')
def select_button(context, button_label):
    if button_label.lower() == "login":
        context.login_page.confirm_login()
    elif button_label.lower() == "cancel":
        context.login_page.cancel_login()
    elif button_label.lower() == "logout":
        context.home_page.logout()


@then('I should see a {error_message} error message')
def verify_error_message(context, error_message):
    assert get_messages_default(error_message) == context.login_page.get_warn_message(), get_messages_default(error_message) + "\n" + context.login_page.get_warn_message()


@then('I should not see the login popup anymore')
def verify_the_login_popup(context):
    assert context.login_page.check_title_invisibility()


@then('I am logged out from the application')
def verify_logout(context):
    assert context.home_page.check_login_button()


@step('I have no network connection')
def turn_the_connection_off(context):
    process = subprocess.Popen(
        "adb shell",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )

