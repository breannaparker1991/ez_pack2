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
  return render_template("trip.html", user = User.get_one(data))
  
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
  Trip.save(data)
  return redirect('/welcome')

@app.route('/destroy/<int:id>')
def destroy_trip(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id' : id
  }
  Trip.destroy(data)
  return redirect('/welcome')
