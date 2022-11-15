from flaskr.app import app
from flaskr.api.colors import api
from flaskr.data_base.FDataBase import dBase
from flaskr.data_base.models import Item
from flask import redirect, url_for, request
from flask_login import login_required, current_user
from flaskr.data_base.models import Operation, OperationTypes
import requests


@app.route("/takeitem", methods=["POST"])
@login_required
def takeitem():

    id: int = int(request.args.get("id", default=0))
    amount: int = int(request.form["Amount"])

    dBase.takeItem(id, amount)

    newOperation: Operation = Operation(user_id=int(
        current_user.get_id()), item_id=id, type=OperationTypes.take, amount=amount)
    dBase.registerNewOperation(newOperation)

    item: Item = dBase.getItemById(id)

    requests.post("http://127.0.0.1/api/colors",
                  data={"cell_id": item.cellId, "color": "#2bf70b"})

    return redirect(url_for("itemslist"))
