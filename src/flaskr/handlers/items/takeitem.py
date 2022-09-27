from flaskr.app import app
from flaskr.data_base.FDataBase import dBase
from flask import redirect, url_for , request
from flask_login import login_required, current_user
from flaskr.data_base.models import Operation, OperationTypes


@app.route("/takeitem", methods = ["POST"])
@login_required
def takeitem():
	id : int = int(request.args.get("id", default=0))
	amount : int = int(request.form["Amount"])
	
	dBase.takeItem(id, amount)
	
	newOperation : Operation = Operation(user_id =int(current_user.get_id()) , item_id = id , type = OperationTypes.take , amount = amount)
	dBase.registerNewOperation(newOperation)
 
	return redirect(url_for("itemslist"))