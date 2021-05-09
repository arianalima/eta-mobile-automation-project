from utils.constants import Messages


def get_messages_default(key):
    messages = Messages()
    return getattr(messages, key.upper())