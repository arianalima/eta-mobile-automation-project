import os
import sys

from behave import step, then

from utils.constants import *
from utils.utils import get_messages_default

PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)


@step('I select the login page')
def open_login_page(context):
    context.home_page.open_login_screen()


@then('I should be able to see all fields displayed')
def verify_login_fields_displayed(context):
    assert Labels.POPUP_TITLE.value, context.login_page.get_title_message()
    assert Labels.USERNAME_LABEL.value, context.login_page.get_username_label()
    assert Labels.PASSWORD_LABEL.value, context.login_page.get_password_label()
    assert Messages.WARN_MESSAGE.value, context.login_page.get_warn_message()
    assert Labels.CANCEL_LABEL.value, context.login_page.get_cancel_button_label()
    assert Labels.LOGIN_LABEL.value, context.login_page.get_login_button_label()


@step('I insert a {user_type} user')
def insert_user(context, user_type):
    if user_type.lower() == "valid":
        context.login_page.insert_username(Credentials.VALID_USERNAME.value)
    elif user_type.lower() == "invalid":
        context.login_page.insert_username(Credentials.INVALID_USERNAME.value)


@step('I insert a {password_type} password')
def insert_password(context, password_type):
    if password_type.lower() == "valid":
        context.login_page.insert_password(Credentials.VALID_PASSWORD_FOR_VALID_USERNAME.value)
    elif password_type.lower() == "invalid":
        context.login_page.insert_password(Credentials.INVALID_PASSWORD.value)
    elif password_type.lower() == "short":
        context.login_page.insert_password(Credentials.SHORT_PASSWORD.value)


@step('I select the {button_label} button')
def select_button(context, button_label):
    if button_label.lower() == "login":
        context.login_page.confirm_login()
    elif button_label.lower() == "cancel":
        context.login_page.cancel_login()


@then('I should see a {error_message} error message')
def verify_error_message(context, error_message):
    expected_message = get_messages_default(error_message)
    actual_message = context.login_page.get_warn_message()
    assert expected_message == actual_message, "Expected: %s\nActual: %s" % (expected_message, actual_message)


@then('I should not see the login popup anymore')
def verify_the_login_popup(context):
    assert context.login_page.get_title_invisibility()


@then('I should see that valid user is logged')
def verify_logged_user(context):
    expected_user = Credentials.VALID_USERNAME.value
    actual_user = context.home_page.get_logged_user()
    assert expected_user == actual_user, "Expected: %s\nActual: %s" % (expected_user, actual_user)


@step('I have no network connection')
def turn_the_connection_off(context):
    os.system("adb shell svc wifi disable")
    os.system("adb shell svc data disable")


@step('I enable the network connection')
def turn_the_connection_on(context):
    os.system("adb shell svc wifi enable")
    os.system("adb shell svc data enable")
