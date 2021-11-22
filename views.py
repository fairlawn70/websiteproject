from flask import Blueprint, render_template, url_for, redirect, request

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("home.html")
