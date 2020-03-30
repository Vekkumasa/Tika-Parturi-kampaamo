from flask import redirect, url_for, render_template, request, flash
from flask_login import login_required

from application import app, db
from application.kampaamo.models import Asiakas, Varaus, Aika
from application.kampaamo.forms import KampaajaForm, AsiakasForm, VarausForm, AikaForm, EditForm, DeleteForm
from application.auth.models import User

@app.route("/kampaaja/", methods=["GET"])
def kampaaja_index():
    return render_template("kampaamo/list.html", kampaajat=User.query.all())

@app.route("/kampaaja/new/")
@login_required
def kampaaja_form():
    return render_template("kampaamo/newKampaaja.html", form = KampaajaForm())

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>", methods=["GET"])
@login_required
def varaus_crud(kampaaja_id, varaus_id):
    return render_template("kampaamo/varaus_CRUD.html", kampaaja=User.query.get(kampaaja_id), varaus=Varaus.find_reservations(varaus_id), form = DeleteForm)

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>/", methods=["POST"])
@login_required
def poista_varaus(varaus_id, kampaaja_id):
    v = Varaus.query.get(varaus_id)
    db.session.delete(v)
    db.session.commit()

    return redirect(url_for("kampaaja_index"))

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>/muokkaa/<aika_id>", methods=["GET"])
@login_required
def varaus_muokkaus(varaus_id, kampaaja_id, aika_id):
    return render_template("kampaamo/varaus_EDIT.html", kampaaja=User.query.get(kampaaja_id), varaus=Varaus.find_reservations(varaus_id), aika = Aika.query.get(aika_id), form = EditForm())

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>/muokkaa/<aika_id>", methods=["POST"])
@login_required
def muokkaa_varausta(varaus_id, kampaaja_id, aika_id):

    form = EditForm(request.form)

    if not form.validate():
        return render_template("kampaamo/varaus_EDIT.html", kampaaja = kampaaja_id , aika = aika_id, varaus=varaus_id, form = form)
    
    aika = Aika.query.get(aika_id)
    aika.pvm = form.pvm.data
    aika.h = form.aika_h.data
    aika.min = form.aika_min.data
    
    db.session.commit()

    return redirect(url_for("kampaaja_index"))

@app.route("/kampaaja/<kampaaja_id>", methods=["GET"])
def kampaaja_show(kampaaja_id):
    return render_template("kampaamo/singleKampaaja.html", kampaaja=User.query.get(kampaaja_id), pvm=User.find_available_times(kampaaja_id), form = VarausForm())

@app.route("/kampaaja/<kampaaja_id>/varaukset", methods=["GET"])
@login_required
def kampaajan_varaukset(kampaaja_id):
    return render_template("kampaamo/omat_varaukset.html", kampaaja=User.query.get(kampaaja_id), varaus=User.find_reservations(kampaaja_id))

@app.route("/kampaaja/<kampaaja_id>/varaus/<aika_id>", methods=["GET"])

def varaus_sivu(kampaaja_id, aika_id):
    return render_template("kampaamo/varausformi.html", kampaaja=User.query.get(kampaaja_id), aika=Aika.query.get(aika_id), form = VarausForm())

@app.route("/kampaaja/<kampaaja_id>/varaus/<aika_id>", methods=["POST"])
def create_varaus(kampaaja_id, aika_id):

    form = VarausForm(request.form)

    a = Asiakas.query.get(form.phoneNumber.data)
    if not a:
        a = Asiakas(form.firstName.data, form.lastName.data, form.phoneNumber.data)

        if form.validate():
            db.session.add(a)
            flash('Varaus tehty nimellä: {} {}'.format(form.firstName.data, form.lastName.data))
        else:
            flash('Varauksen teko epäonnistui:')
            return render_template("kampaamo/varausformi.html", kampaaja = kampaaja_id, aika = aika_id, form = form)
    v = Varaus()

    aika = Aika.query.get(aika_id)
    aika.vapaa = False

    v.kampaaja_id = kampaaja_id
    v.asiakas_id = a.phoneNumber
    v.aika_id = aika.id

    db.session.add(v)
    db.session.commit()

    return render_template("kampaamo/varausformi.html", kampaaja = kampaaja_id, aika = aika_id, form = form)

@app.route("/kampaaja/<kampaaja_id>/aika", methods=["GET"])
@login_required
def aika(kampaaja_id):
    return render_template("kampaamo/ajanvaraus.html", kampaaja=User.query.get(kampaaja_id), form = AikaForm())

@app.route("/kampaaja/<kampaaja_id>/aika", methods=["POST"])
@login_required
def create_aika(kampaaja_id):

    form = AikaForm(request.form)

    if not form.validate():
        flash('Ajan lisääminen epäonnistui')
        return render_template("kampaamo/ajanvaraus.html", kampaaja = kampaaja_id ,form = form)

    a = Aika(form.pvm.data, form.aika_h.data, form.aika_min.data, kampaaja_id)

    db.session.add(a)
    db.session.commit()

    flash('Aika lisätty: {} {} {}'.format(form.pvm.data, form.aika_h.data, form.aika_min.data))
    return redirect(url_for("create_aika", kampaaja_id=kampaaja_id))

@app.route("/kampaaja/", methods=["POST"])
@login_required
def kampaaja_create():

    form = KampaajaForm(request.form)

    if not form.validate():
        flash('Kampaajan lisääminen epäonnistui')
        return render_template("kampaamo/newKampaaja.html", form = form)

    k = User(form.name.data, form.username.data, form.password.data)

    db.session().add(k)
    db.session().commit()

    flash('Kampaaja lisätty: {} {}'.format(form.name.data, form.username.data))
    return redirect(url_for("kampaaja_form"))


@app.route("/asiakas/", methods=["GET"])
def asiakas_index():
    return render_template("kampaamo/asiakkaat.html", asiakkaat=Asiakas.query.all())

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