from flask import render_template,redirect,request
from flask_app import app
# from flask_app.models.dojo import Dojo
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
# dojo is file and Dojo is class, importing dojo file to access the Dojo.get_all
    return render_template('ninja.html',dojos=dojo.Dojo.get_all())

@app.route('/new/ninja',methods=['POST'])
def new_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')