from flask_app import app
from flask import redirect, request, render_template, session, flash
from flask_app.models.user import User
from flask_app.models.list import List
from flask_app.models.trip import Trip
from flask_app.models.item import Item



@app.route('/destroy/item/<int:id>')
def destroy_items(id):
  if 'user_id' not in session:
    return redirect('/logout')
  data = {
    'id' : id
  }
  Item.destroy(data)
  return redirect('/welcome')


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
    'user_id': session['user_id'],
  }
  list = List.save(data)
  print(list)
  return redirect(f'/add/items/{list}')

@app.route('/add/items/<int:id>')
def add_items(id):
  if 'user_id' not in session:
    return redirect ('/logout')
  data = {
    'id': id
  }
  user = {
    'id': session['user_id'], 
  }
  list = List.get_one(data)
  user = User.get_one(user)
  return render_template('items.html', list = list, user = user)

@app.route('/more/items', methods=['POST'])
def more():
  if 'user_id' not in session:
    return redirect ('/logout')
  print(request.form)
  data = {
    'name': request.form['name'],
    # 'id': session['list_id']
  }
  Item.save(data)
  return redirect('/add/items/<ind:id>')
