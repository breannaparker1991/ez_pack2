from flask import flash
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Item:
  db = 'ez_pack'
  def __init__ (self, db_data):
    self.id = db_data['id']
    self.name = db_data['name']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    self.list_id = db_data['list_id']
    self.list_user_id = db_data['list_user_id']
    self.list_trip_id = db_data['list_trip_id']  