from flask import Blueprint, render_template, url_for

admin = Blueprint("admin", __name__)

@admin.route("/")
@admin.route("/dashboard", methods=[""])
def dashboard():
    return render_template("admin/main.html")