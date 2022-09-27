from flaskr.app import app
from flask_login import login_required, current_user
from flask import render_template
from ..loginmanager.loginmanager import login_manager
from flaskr.data_base.FDataBase import dBase
from flaskr.data_base.models import Operation , OperationTypes



@app.route("/userpage")
@login_required
def userpage():

    operations : list[dict] = []
    
    for operation in dBase.getUserOperations(int(current_user.get_id())):
        
        operations.append({
            "type" : "Взятие" if operation.type == OperationTypes.take else "Добавление" ,
            "item_name" :  dBase.getItemById(operation.item_id).title,
            "item_id" : operation.item_id,
            "amount" : operation.amount
        })

    return render_template("userpage.html", operations=operations)