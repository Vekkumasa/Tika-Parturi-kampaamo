from flask import redirect, url_for, render_template, request
from flask_login import login_required

from application import app, db
from application.kampaamo.models import Asiakas, Varaus, Aika
from application.kampaamo.forms import KampaajaForm, AsiakasForm, EditForm, VarausForm, AikaForm
from application.auth.models import User

@app.route("/kampaaja/", methods=["GET"])
def kampaaja_index():
    return render_template("kampaamo/list.html", kampaajat=User.query.all())

@app.route("/kampaaja/new/")
@login_required
def kampaaja_form():
    return render_template("kampaamo/newKampaaja.html", form = KampaajaForm())

@app.route("/kampaaja/<kampaaja_id>", methods=["GET"])
def kampaaja_show(kampaaja_id):
    return render_template("kampaamo/singleKampaaja.html", kampaaja=User.query.get(kampaaja_id), form = VarausForm())


@app.route("/kampaaja/<kampaaja_id>", methods=["POST"])
def create_varaus(kampaaja_id):

    form = VarausForm(request.form)

    a = Asiakas.query.get(form.phoneNumber.data)
    v = Varaus()

    v.kampaaja_id = kampaaja_id
    v.asiakas_id = a.phoneNumber
    v.varaus_pvm = form.date.data

    db.session.add(v)
    db.session.commit()

    return redirect(url_for("kampaaja_index"))

@app.route("/kampaaja/<kampaaja_id>/aika", methods=["GET"])
def aika(kampaaja_id):
    return render_template("kampaamo/ajanvaraus.html", kampaaja=User.query.get(kampaaja_id), form = AikaForm())

@app.route("/kampaaja/<kampaaja_id>/aika", methods=["POST"])
def create_aika(kampaaja_id):

    form = AikaForm(request.form)

    a = Aika(form.pvm.data, form.aika_h.data, form.aika_min.data, kampaaja_id)

    db.session.add(a)
    db.session.commit()

    return redirect(url_for("aika", kampaaja_id=kampaaja_id))

@app.route("/kampaaja/", methods=["POST"])
@login_required
def kampaaja_create():

    form = KampaajaForm(request.form)

    if not form.validate():
        return render_template("kampaamo/newKampaaja.html", form = form)

    k = User(form.name.data, form.username.data, form.password.data)

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

    if not form.validate():
        return render_template("kampaamo/newAsiakas.html", form = form)

    asiakas = Asiakas.query.get(form.phoneNumber.data)

    if asiakas:
        return render_template("kampaamo/newAsiakas.html", form = form, uniikki = "Puhelinnumero on jo käytössä")

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
    return render_template("kampaamo/singleAsiakas.html", asiakas=Asiakas.query.get(asiakas_id))