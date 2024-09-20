from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/projects")
def profolio():
    return render_template("projects.html")

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))