from flask import render_template
from auth import auth_bp
from auth.forms import LoginForm


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)
