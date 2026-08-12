def validate_username(username):
    if not isinstance(username, str):
        raise ValueError('Username must be a string')
    if not (3 <= len(username) <= 20):
        raise ValueError('Username must be between 3 and 20 characters')
    if not username.isalnum():
        raise ValueError('Username must only contain alphanumeric characters')
    return True


def validate_password(password):
    if not isinstance(password, str):
        raise ValueError('Password must be a string')
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters long')
    if not any(char.isdigit() for char in password):
        raise ValueError('Password must contain at least one digit')
    if not any(char.isupper() for char in password):
        raise ValueError('Password must contain at least one uppercase letter')
    return True


def validate_email(email):
    import re
    if not isinstance(email, str):
        raise ValueError('Email must be a string')
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not email_regex.match(email):
        raise ValueError('Invalid email format')
    return True