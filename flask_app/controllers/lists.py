from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.list import List
from flask_app.models.trip import Trip

@app.route('/create')
def new():
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id': session['user_id']
  }
  return render_template("create.html", user = User.get_one(data))

@app.route('/create/list', methods= ['POST'])
def create():
  if 'user_id' not in session:
    return redirect ('/logout')
  if not List.validate(request.form):
    print('oops, theres a problem')
    return redirect('/new')
  print(request.form)
  data = {
    'name': request.form['name'],
    'description': request.form['description'],
    'item': request.form['item'],
    'user_id': session['user_id'],
  }
  list = List.save(data)
  print(list)
  return redirect('/welcome')

@app.route('/destroy/list/<int:id>')
def destroy_list(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id' : id
  }
  List.destroy(data)
  return redirect('/welcome')

@app.route('/edit/<int:id>')
def edit(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id': id
  }
  user = {
    'id': session['user_id']
    
  }
  list = List.get_one(data)
  user = User.get_one(user)
  # items = Item.get_all()
  return render_template("edit.html", list = list, user = user)
  
@app.route('/update', methods= ['POST'])
def update():
  if 'user_id' not in session:
    return redirect ('/logout')
  if not List.validate(request.form):
    return redirect('/create/list')
  data = {
    'name': request.form['name'],
    'description': request.form['description'],
    'item': request.form['item'], 
    'id': session['user_id'],
  }
  List.update(data)
  # Item.update(data)
  return redirect('/welcome')