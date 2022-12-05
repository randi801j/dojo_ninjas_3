from flask_app import app
from flask import render_template, redirect,request
from flask_app.models.dojo import Dojo


@app.route('/')
def home():
    return redirect ('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('home.html',all_dojos=dojos)

@app.route('/new/dojo',methods=['POST'])
def new_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data={'id':id}
    return render_template('dojo.html',dojo=Dojo.get_ninja_datas(data))