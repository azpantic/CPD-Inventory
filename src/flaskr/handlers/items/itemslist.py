from re import search
from flaskr.app import app
from flask_login import login_required
from flask import render_template , request

from flaskr.data_base.models import Item
from ...data_base.FDataBase import dBase

@app.route("/itemslist" , methods = ["GET" , "POST"])
@login_required
def itemslist():
    items = dBase.getItemsByPage(1)
    
    if request.method == "POST":
        search = request.form.get("Search" , default="")
        items = dBase.searchForItems(search)
    
    return render_template("itemslist.html", items = items)