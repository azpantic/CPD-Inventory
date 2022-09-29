
from flaskr.app import app
from flask import render_template , request
from flask_login import login_required

from flaskr.data_base.models import Item
from flaskr.data_base.FDataBase import dBase
from ...loginmanager.loginmanager import administrator_required

@app.route("/createitem", methods = ["POST" , "GET"])
@login_required
@administrator_required
def createitem():
    
    if request.method == "POST":
        
        form = request.form
        title  = form["Title"]
        cellId = form["CellId"]
        amount = form["Amount"]
        description = form["Description"]
        newItem : Item = Item(title= title , cellId = cellId, count = amount , description=description )
        
        dBase.createItem(newItem)
        
    return render_template("creatitem.html")