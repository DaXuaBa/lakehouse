import re

def is_valid_username(username):
    if not isinstance(username, str):
        return False

    pattern = r'^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$'

    if re.match(pattern, username):
        return True
    return False