from flask import redirect, url_for, render_template, request, flash
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User
from application.varaus.forms import VarausForm, DeleteForm
from application.varaus.models import Varaus
from application.aika.forms import EditForm, DeleteTimeForm
from application.aika.models import Aika
from application.asiakas.forms import AsiakasForm
from application.asiakas.models import Asiakas

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>", methods=["GET"])
@login_required
def varaus_crud(kampaaja_id, varaus_id):
    return render_template("varaus/varaus_CRUD.html", kampaaja=User.query.get(kampaaja_id), varaus=Varaus.find_reservations(varaus_id), form = DeleteForm)

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>/", methods=["POST"])
@login_required
def poista_varaus(varaus_id, kampaaja_id):
    v = Varaus.query.get(varaus_id)
    a = Aika.query.get(v.aika_id)
    a.vapaa = 1
    db.session.delete(v)
    db.session.commit()

    return redirect(url_for("kampaaja_index"))


@app.route("/kampaaja/<kampaaja_id>/varaus/<aika_id>", methods=["GET"])
def varaus_sivu(kampaaja_id, aika_id):
    return render_template("varaus/varausformi.html", kampaaja=User.query.get(kampaaja_id), aika=Aika.query.get(aika_id), formi = DeleteTimeForm(), form = VarausForm())


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
            return render_template("varaus/varausformi.html", kampaaja = kampaaja_id, aika = aika_id, form = form)
    

    aika = Aika.query.get(aika_id)
    aika.vapaa = 0

    v = Varaus(kampaaja_id, a.phoneNumber, aika.id)

    db.session.add(v)
    db.session.commit()

    return render_template("varaus/varausformi.html", kampaaja = kampaaja_id, aika = aika_id, form = form)