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