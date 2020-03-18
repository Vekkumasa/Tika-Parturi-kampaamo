from application import app, db
from flask import redirect, url_for, render_template, request

from application.kampaamo.models import Kampaaja, Asiakas
from application.kampaamo.forms import KampaajaForm, AsiakasForm, EditForm

@app.route("/kampaaja/", methods=["GET"])
def kampaaja_index():
    return render_template("kampaamo/list.html", kampaajat=Kampaaja.query.all())

@app.route("/kampaaja/new/")
def kampaaja_form():
    return render_template("kampaamo/newKampaaja.html", form = KampaajaForm())

@app.route("/kampaaja/", methods=["POST"])
def kampaaja_create():

    form = KampaajaForm(request.form)

    if not form.validate():
        return render_template("kampaamo/newKampaaja.html", form = form)

    k = Kampaaja(form.firstName.data, form.lastName.data)

    db.session().add(k)
    db.session().commit()

    return redirect(url_for("kampaaja_index"))

@app.route("/asiakas/", methods=["GET"])
def asiakas_index():
    return render_template("kampaamo/asiakkaat.html", asiakkaat=Asiakas.query.all(), form = EditForm)

@app.route("/asiakas/new/")
def asiakas_form():
    return render_template("kampaamo/newAsiakas.html", form = AsiakasForm())

@app.route("/asiakas/", methods=["POST"])
def asiakas_create():

    form = AsiakasForm(request.form)

    a = Asiakas(form.firstName.data, form.lastName.data, form.phoneNumber.data)

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("asiakas_index"))

@app.route("/asiakas/<asiakas_id>/", methods=["POST"])
def asiakas_change_number(asiakas_id):
    
    number = request.form.get("number")
    a = Asiakas.query.get(asiakas_id)
    a.phoneNumber = number
    db.session().commit()

    return redirect(url_for("asiakas_index"))
