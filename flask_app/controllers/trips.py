from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.list import List
from flask_app.models.trip import Trip


@app.route('/trip')
def trip():
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id': session['user_id']
  }
  user = User.get_one(data)
  return render_template("trip.html", user = user)
  
@app.route('/new/trip', methods= ['POST'])
def new_trip():
  if 'user_id' not in session:
    return redirect ('/logout')
  if not Trip.validate(request.form):
    print('oops, theres a problem')
    return redirect('/new')
  print(request.form)
  data = {
    'name': request.form['name'],
    'description': request.form['description'],
    'date_range': request.form ['date_range'],
    'user_id': session['user_id'],
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
  lists = List.get_all()
  user = User.get_one(user)
  trip = Trip.get_one(data)
  return render_template('list_trip.html', lists = lists, user = user, trip = trip)

@app.route('/list/trip/insert/<int:id>', methods = ['POST'])
def list_trip_insert(id):
  if 'user_id' not in session:
    return redirect ('/logout')
  for form in request.form.getlist('list_id'):
    data = {
      'list_id': form,
      'trip_id': id
    }
    Trip.insert(data)
  return redirect('/welcome')

@app.route('/destroy/trip/<int:id>')
def destroy_trip(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id' : id
  }
  Trip.destroy(data)
  return redirect('/welcome')
