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
    
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM item;"
    results = connectToMySQL(cls.db).query_db(query)
    recipes = []
    for r in results:
      recipes.append(cls(r))
    return recipes
  
  @classmethod
  def save(cls,data):
    query = "INSERT INTO recipe (name) VALUES (%(name)s);"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM list WHERE list.id = %(id)s;"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def get_one(cls,data):
    query = "SELECT * FROM list WHERE id = %(id)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    if len(results) < 1:
      return False
    return cls(results[0])
  
  @classmethod
  def update(cls,data):
    query = "UPDATE list SET name=%(name)s, updated_at = NOW() WHERE id = %(id)s;"
    return connectToMySQL(cls.db).query_db(query,data)

  @staticmethod
  def validate(item):
    validate = True
    if len(item['name']) > 20:
      flash('Item name cannot be more than 20 characters long', 'name')
      validate = False
    return validate