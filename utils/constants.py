from enum import Enum


class Credentials(Enum):
    VALID_USERNAME = "dummy123"
    VALID_PASSWORD_FOR_VALID_USERNAME = "dummy123"
    INVALID_USERNAME = "dummy"
    INVALID_PASSWORD = "dummy000"
    SHORT_PASSWORD = "123"


class Messages(Enum):
    ERROR_MESSAGE_INVALID_USER = "Arrr…wrong username/password"
    ERROR_MESSAGE_SHORT_PASSWORD = "You got a short…password"
    ERROR_MESSAGE_EMPTY_LOGIN = "Catch you, anonymous!"
    ERROR_MESSAGE_NO_NETWORK = "Where's the Internet? Can't get it"
    LOGIN_SUCCESS_MESSAGE = "Login succeed"
    WARN_MESSAGE = "* Your password will NOT be saved"


class Labels(Enum):
    USERNAME_LABEL = "Username"
    PASSWORD_LABEL = "Password"
    CANCEL_LABEL = "CANCEL"
    LOGIN_LABEL = "LOGIN"
    POPUP_TITLE = "Login"
