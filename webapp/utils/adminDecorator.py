from functools import wraps
from flask.helpers import flash
from flask_login import current_user
from flask import request, redirect, url_for


def admin_protected(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(current_user.role)
        if current_user.role.lower() != "Admin".lower():
            flash("Sorry! Only admins can access this route! Please login with your admin account to continue!", category="error")
            return redirect(url_for("authviews.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function