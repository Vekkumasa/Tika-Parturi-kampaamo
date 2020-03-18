from application import app, db
from flask import redirect, url_for, render_template, request

from application.kampaamo.models import Kampaaja
from application.kampaamo.forms import KampaajaForm

@app.route("/kampaaja/", methods=["GET"])
def kampaaja_index():
    return render_template("kampaamo/list.html", kampaajat=Kampaaja.query.all())

@app.route("/kampaaja/new/")
def kampaaja_form():
    return render_template("kampaamo/new.html", form = KampaajaForm())

@app.route("/kampaaja/", methods=["POST"])
def kampaaja_create():

    form = KampaajaForm(request.form)

    if not form.validate():
        return render_template("kampaamo/new.html", form = form)

    k = Kampaaja(form.firstName.data, form.lastName.data)

    db.session().add(k)
    db.session().commit()

    return redirect(url_for("kampaaja_index"))