from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.list import List
from flask_app.models.trip import Trip
from flask_app.models.item import Item
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/register/now', methods =['POST'])
def register_now():
  if not User.validate(request.form):
    return redirect('/')
  pw_hash = bcrypt.generate_password_hash(request.form['password'])
  print(pw_hash)
  data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email':request.form['email'],
    'password': pw_hash
  }
  id = User.save(data)
  if not id:
    flash("Email already taken, please register")
    return redirect('/')
  session['user_id'] = id
  return redirect ('/welcome')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/login/now', methods = ['POST'])
def login_now():
  data = {'email': request.form['email']}
  user_in_db = User.get_email(data)
  if not user_in_db:
    flash('invalid Email/Password', 'login')
    return redirect('/')
  if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    flash("Invalid Email/Password", 'login') 
    return redirect('/')
  session['user_id'] = user_in_db.id
  return redirect ('/welcome')

@app.route('/welcome')
def welcome():
  if 'user_id' not in session:
    return redirect ('/logout')
  data = {
    'id':session['user_id']
  }
  lists = List.get_all()
  user = User.get_one(data)
  trips = Trip.get_all()
  return render_template("welcome.html", lists = lists, user = user, trips = trips)


@app.route('/logout') 
def logout():
  session.clear()
  return redirect('/')