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


  @classmethod
  def save(cls,data):
    query = "INSERT INTO list (name, description, user_id) VALUES ( %(name)s, %(description)s, %(user_id)s);"
    return connectToMySQL(cls.db).query_db(query,data) 

  @classmethod
  def get_one(cls,data):
    query = "SELECT * FROM list WHERE id = %(id)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    if len(results) < 1:
      return False
    return cls(results[0])
  
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM list;"
    results = connectToMySQL(cls.db).query_db(query)
    recipes = []
    for r in results:
      recipes.append(cls(r))
    return recipes
  
  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM list WHERE list.id = %(id)s;"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def update(cls,data):
    query = "UPDATE list SET name=%(name)s, description = %(description)s;"
    return connectToMySQL(cls.db).query_db(query,data)

  @staticmethod
  def validate(list):
    validate = True
    if len(list['name']) > 20:
      flash('List name cannot be more than 20 characters long', 'name')
      validate = False
    return validate