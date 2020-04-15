from flask import redirect, url_for, render_template, request, flash
from flask_login import login_required

from application import app, db
from application.auth.models import User
from application.varaus.forms import VarausForm, DeleteForm
from application.varaus.models import Varaus
from application.kampaaja.forms import KampaajaForm

@app.route("/kampaaja/", methods=["GET"])
def kampaaja_index():
    return render_template("kampaaja/list.html", kampaajat=User.query.all())

@app.route("/kampaaja/new/")
@login_required
def kampaaja_form():
    return render_template("kampaaja/newKampaaja.html", form = KampaajaForm())

@app.route("/kampaaja/<kampaaja_id>", methods=["GET"])
def kampaaja_show(kampaaja_id):
    return render_template("kampaaja/singleKampaaja.html", kampaaja=User.query.get(kampaaja_id), pvm=User.find_available_times(kampaaja_id), form = VarausForm())

@app.route("/kampaaja/<kampaaja_id>/varaukset", methods=["GET"])
@login_required
def kampaajan_varaukset(kampaaja_id):
    return render_template("kampaaja/omat_varaukset.html", kampaaja=User.query.get(kampaaja_id), varaus=User.find_reservations(kampaaja_id))

@app.route("/kampaaja/", methods=["POST"])
@login_required
def kampaaja_create():

    form = KampaajaForm(request.form)

    if not form.validate():
        flash('Kampaajan lisääminen epäonnistui')
        return render_template("kampaaja/newKampaaja.html", form = form)

    k = User(form.name.data, form.username.data, form.password.data)

    db.session().add(k)
    db.session().commit()

    flash('Kampaaja lisätty: {} {}'.format(form.name.data, form.username.data))
    return redirect(url_for("kampaaja_form"))