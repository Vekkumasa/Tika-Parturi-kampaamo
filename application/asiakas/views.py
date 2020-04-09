from flask import redirect, url_for, render_template, request, flash
from flask_login import login_required

from application import app, db
from application.auth.models import User
from application.varaus.forms import VarausForm, DeleteForm
from application.varaus.models import Varaus
from application.kampaaja.forms import KampaajaForm
from application.aika.models import Aika
from application.aika.forms import AikaForm, EditForm, DeleteTimeForm
from application.asiakas.forms import AsiakasForm
from application.asiakas.models import Asiakas

@app.route("/asiakas/", methods=["GET"])
def asiakas_index():
    return render_template("asiakas/asiakkaat.html", asiakkaat=Asiakas.query.all())

@app.route("/asiakas/new/")
def asiakas_form():
    return render_template("asiakas/newAsiakas.html", form = AsiakasForm())

@app.route("/asiakas/", methods=["POST"])
def asiakas_create():

    form = AsiakasForm(request.form)

    if not form.validate():
        return render_template("asiakas/newAsiakas.html", form = form)

    asiakas = Asiakas.query.get(form.phoneNumber.data)

    if asiakas:
        return render_template("asiakas/newAsiakas.html", form = form, uniikki = "Puhelinnumero on jo käytössä")

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

@app.route("/asiakas/<asiakas_id>", methods=["GET"])
def asiakas_show(asiakas_id):
    return render_template("asiakas/singleAsiakas.html", asiakas=Asiakas.query.get(asiakas_id))