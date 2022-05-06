from flask import flash
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Trip:
  db = 'ez_pack'
  def __init__ (self, db_data):
    self.id = db_data['id']
    self.name = db_data['name']
    self.description = db_data['description']
    self.date_range = db_data['date_range']
    self.updated_at = db_data['updated_at']
    self.created_at = db_data['created_at']  
    self.user_id = db_data['user_id']