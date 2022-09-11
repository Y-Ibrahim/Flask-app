from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
        return "Login"


@auth.route("/sign-up")
def signUp():
        return "Sign Up"

@auth.route("/logout")
def logout():
        return "Log Out"
    