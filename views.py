from flask import Blueprint, render_template, url_for, redirect, request, send_file

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/home")
def landing():
    return redirect(url_for('views.home'))


@views.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")


@views.route("/academic")
def academic():
    return render_template("academic.html")


@views.route("/artphoto")
def artphoto():
    return render_template("artphoto.html")


@views.route("/athletic")
def athletic():
    return render_template("athletic.html")


@views.route("/mybook")
def mybook():
    return render_template("book.html")


@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/download")
def download_file():
    p = "Michael_Natenzon_Resume.pdf"
    return send_file(p, as_attachment=True)
