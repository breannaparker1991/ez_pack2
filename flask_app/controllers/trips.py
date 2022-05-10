from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.list import List
from flask_app.models.trip import Trip
from flask_app.models.item import Item


app.route('/trip')
def new():
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id': session['user_id']
  }
  lists = List.get_all()
  user = User.get_one(data)
  return render_template("trip.html", user = user, lists = lists)
  
@app.route('/new/trip', methods= ['POST'])
def new_trip():
  if 'user_id' not in session:
    return redirect ('/logout')
  if not List.validate(request.form):
    print('oops, theres a problem')
    return redirect('/new')
  print(request.form)
  data = {
    'name': request.form['name'],
    'description': request.form['description'],
  }
  trip = Trip.save(data)
  return redirect(f'/list/trip/{trip}')

@app.route('/list/trip/<int:id>')
def list_trip(id):
  if 'user_id' not in session:
    return redirect ('/logout')
  data = {
    'id': id
  }
  user = {
    'id': session['user_id'], 
  }
  list = List.get_one(data)
  items = Item.get_all()
  user = User.get_one(user)
  return render_template('final_trip.html', list = list, items = items, user = user)

@app.route('/destroy/trip/<int:id>')
def destroy_trip(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id' : id
  }
  Trip.destroy(data)
  return redirect('/welcome')
