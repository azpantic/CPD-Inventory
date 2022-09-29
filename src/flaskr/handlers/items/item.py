from flaskr.app import app
from flask import render_template, request 

from flaskr.data_base.models import Item, OperationTypes
from ...data_base.FDataBase import dBase
from flask_login import login_required , current_user

@app.route("/item")
@login_required
def item():
    
    id = request.args.get("id" , default=0)
    item = dBase.getItemById(id)
    operations_history : list[dict] = []
    
    if current_user.is_administrator():
        
        for operation in dBase.getItemOperationsHistory(id):
            operations_history.append({
                "type" : "Взятие" if operation.type == OperationTypes.take else "Добавление",
                "amount" :operation.amount , 
                "user_name" : dBase.getUserById(operation.user_id).name,
                "user_id" : operation.user_id
            })
        
    
    return render_template("item.html", item = item , operations_history = operations_history)