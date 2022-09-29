from re import search
from flaskr.app import app
from flask_login import login_required
from flask import render_template , request

from flaskr.data_base.models import Item
from ...data_base.FDataBase import dBase

@app.route("/itemslist" , methods = ["GET" , "POST"])
@login_required
def itemslist():
    items = dBase.getItemsByPage(1, True , False)
    
    if request.method == "POST":
        search = request.form.get("Search" , default="")
        only_available = request.form.get("OnlyAvailable" , default="") == "on"
        search_disable = request.form.get("SearchDisable" , default="") == "on"
        items = dBase.searchForItems(search, only_available , search_disable)
    
    return render_template("itemslist.html", items = items)