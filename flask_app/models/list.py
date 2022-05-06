from msilib.schema import Class
from sqlite3 import dbapi2
from flask import flash
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class List:
  db = 'ez_pack'
  def __init__ (self, db_data):
    self.id = db_data['id']
    self.name = db_data['name']
    self.description = db_data['description']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    self.user_id = db_data['user_id']
    self.trip_id = db_data['trip_id']
