from flask_app import app
from flask_app.controllers import users, trips, items, lists

if __name__ =="main":
  app.run(debug=True)
  
  