from flaskr.app import app
from flaskr.data_base.FDataBase import dBase
from flaskr.data_base.models import Operation , OperationTypes
from flask import request, redirect , url_for
from flask_login import login_required , current_user

@app.route("/additem" , methods = ["POST"])
@login_required
def additem():
    
	id : int = int(request.args.get("id", default=0))
	amount : int = int(request.form["Amount"])
	
	dBase.addItem(id, amount)
	
	newOperation : Operation = Operation(user_id =int(current_user.get_id()) , item_id = id , type = OperationTypes.add , amount = amount)
	dBase.registerNewOperation(newOperation)
 
	return redirect(url_for("itemslist"))
    