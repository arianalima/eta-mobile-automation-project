from enum import Enum


class Messages(Enum):
    ERROR_MESSAGE_INVALID_USER = "Arrr…wrong username/password"
    ERROR_MESSAGE_SHORT_PASSWORD = "You got a short…password"
    ERROR_MESSAGE_EMPTY_LOGIN = "Catch you, anonymous!"
    ERROR_MESSAGE_NO_NETWORK = "Where's the Internet? Can't get it"
    LOGIN_SUCCESS_MESSAGE = "Login succeed"
