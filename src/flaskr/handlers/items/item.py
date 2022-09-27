from flaskr.app import app
from flask import render_template, request 

from flaskr.data_base.models import Item
from ...data_base.FDataBase import dBase
from flask_login import login_required

@app.route("/item")
@login_required
def item():
    
    id = request.args.get("id" , default=0)
    item = dBase.getItemById(id)
    return render_template("item.html", item = item)