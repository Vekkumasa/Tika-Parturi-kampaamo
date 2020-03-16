from application import app, db
from flask import redirect, url_for, render_template, request
from application.kampaamo.models import Kampaaja

@app.route("/kampaaja/", methods=["GET"])
def kampaaja_index():
    return render_template("kampaamo/list.html", kampaajat=Kampaaja.query.all())

@app.route("/kampaaja/new/")
def kampaaja_form():
    return render_template("kampaamo/new.html")

@app.route("/kampaaja/", methods=["POST"])
def kampaaja_create():

    k = Kampaaja(request.form.get("firstName"), request.form.get("lastName"))

    db.session().add(k)
    db.session().commit()

    return redirect(url_for("kampaaja_index"))