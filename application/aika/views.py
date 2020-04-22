from flask import redirect, url_for, render_template, request, flash
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User
from application.varaus.forms import VarausForm, DeleteForm
from application.varaus.models import Varaus
from application.kampaaja.forms import KampaajaForm
from application.aika.models import Aika
from application.aika.forms import AikaForm, EditForm, DeleteTimeForm, WorkDayForm
from application.asiakas.models import Asiakas
from application.asiakas.forms import AsiakasForm

@app.route("/kampaaja/<kampaaja_id>/vapaat_ajat", methods=["GET"])
@login_required
def omat_ajat(kampaaja_id):
    return render_template("aika/omat_ajat.html", kampaaja = User.query.get(kampaaja_id), aika = Aika.vapaat_ajat(kampaaja_id), form = DeleteTimeForm())

@app.route("/kampaaja/<kampaaja_id>/vapaat_ajat/<aika_id>", methods=["POST"])
@login_required
def poista_vapaa_aika(kampaaja_id, aika_id):

    aika = Aika.query.get(aika_id)
    db.session.delete(aika)
    db.session.commit()

    return redirect(url_for("omat_ajat", kampaaja_id=kampaaja_id))

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>/muokkaa/<aika_id>", methods=["POST"])
@login_required
def muokkaa_varausta(varaus_id, kampaaja_id, aika_id):

    form = EditForm(request.form)

    if not form.validate():
        flash('Ajan muokkaus epäonnistui')
        return redirect(url_for("varaus_muokkaus", kampaaja_id=kampaaja_id, aika_id = aika_id, varaus_id = varaus_id))
    
    aika = Aika.query.get(aika_id)
    aika.pvm = form.pvm.data
    aika.aika_h = form.aika_h.data
    aika.aika_min = form.aika_min.data
    
    db.session.commit()

    flash('Aika muutettu: {} {} {}'.format(form.pvm.data, form.aika_h.data, form.aika_min.data))
    return redirect(url_for("varaus_muokkaus", kampaaja_id=kampaaja_id, aika_id = aika_id, varaus_id = varaus_id))

@app.route("/kampaaja/<kampaaja_id>/tyopaiva", methods=["GET"])
@login_required
def tyopaiva(kampaaja_id):
    return render_template("aika/create_workday.html", kampaaja=User.query.get(kampaaja_id), form = WorkDayForm())

@app.route("/kampaaja/<kampaaja_id>/<varaus_id>/muokkaa/<aika_id>", methods=["GET"])
@login_required
def varaus_muokkaus(varaus_id, kampaaja_id, aika_id):
    return render_template("aika/varaus_EDIT.html", kampaaja=User.query.get(kampaaja_id), varaus=Varaus.find_reservations(varaus_id), aika = Aika.query.get(aika_id), form = EditForm())

@app.route("/kampaaja/<kampaaja_id>/aika", methods=["GET"])
@login_required
def aika(kampaaja_id):
    return render_template("aika/create_aika.html", kampaaja=User.query.get(kampaaja_id), form = AikaForm())

@app.route("/kampaaja/<kampaaja_id>/aika", methods=["POST"])
@login_required
def create_vapaa_aika(kampaaja_id):

    form = AikaForm(request.form)

    if not form.validate():
        flash('Ajan lisääminen epäonnistui')
        return render_template("aika/create_aika.html", kampaaja = kampaaja_id ,form = AikaForm)

    a = Aika(form.pvm.data, form.aika_h.data, form.aika_min.data, kampaaja_id)
    db.session.add(a)
    db.session.commit()

    flash('Aika lisätty: {} {} {}'.format(form.pvm.data, form.aika_h.data, form.aika_min.data))
    return redirect(url_for("aika", kampaaja_id=kampaaja_id))

@app.route("/kampaaja/<kampaaja_id>/tyopaiva", methods=["POST"])
@login_required
def create_aika(kampaaja_id):

    form = WorkDayForm(request.form)

#    if not form.validate():
#        flash('Päivän lisääminen epäonnistui')
#        return render_template("aika/create_workday.html", kampaaja = User.query.get(kampaaja_id) ,form = WorkDayForm)

    pvm = form.pvm.data
    h = form.aloitusAika.data
    m = 10

    i = 0
    while i < form.kesto.data:
        a1 = Aika(pvm, h, m, kampaaja_id)
        m = 40
        a2 = Aika(form.pvm.data, h, m, kampaaja_id)
        db.session.add(a1)
        db.session.commit()
        db.session.add(a2)
        db.session.commit()
        m = 10
        h += 1
        i += 1
    
    flash('Työpäivä lisätty: {} {} {}'.format(form.pvm.data, form.aloitusAika.data, form.kesto.data))
    return redirect(url_for("create_aika", kampaaja_id=kampaaja_id))