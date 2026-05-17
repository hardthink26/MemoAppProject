from flask import render_template, request, redirect, url_for, session

from auth import auth_bp
from extensions import db
from models import User

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    username = None 
    password = None 
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        session["username"] = username
        return redirect(url_for("index"))

    return render_template("auth/login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User(username=username)
        user.password = password
        db.session.add(user)
        db.session.commit()
        session["username"] = username
        return redirect(url_for("index"))

    return render_template("auth/register.html")

