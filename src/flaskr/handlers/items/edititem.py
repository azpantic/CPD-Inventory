from flaskr.app import app
from flask import redirect, request, url_for
from ...data_base.FDataBase import dBase
from ...data_base.models import Item
from flask_login import login_required

@app.route("/edititem", methods=["POST"])
@login_required
def edititem():
    id = int(request.args.get("id", default=0))

    form = request.form
    title = form["Title"]
    cellId = form["CellId"]
    amount = form["Amount"]
    description = form["Description"]
    newItem : Item = Item(id = id, title=title, cellId=cellId,
                         count=amount, description=description)

    dBase.changeItem(id, newItem)

    return redirect(url_for("item", id=id))
