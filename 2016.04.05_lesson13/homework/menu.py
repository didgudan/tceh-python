from flask.ext.login import current_user

def is_user_active():
    if current_user.is_authenticated:
        return True
    else:
        return False

def is_user_not_active():
    return not is_user_active()