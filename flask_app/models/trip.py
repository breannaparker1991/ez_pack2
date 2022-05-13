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
    
    
  @classmethod
  def save(cls,data):
    query = "INSERT INTO trip (name, description, date_range, user_id) VALUES ( %(name)s, %(description)s, %(date_range)s, %(user_id)s );"
    return connectToMySQL(cls.db).query_db(query,data) 

  @classmethod
  def get_one(cls,data):
    query = "SELECT * FROM trip WHERE id = %(id)s;"
    results = connectToMySQL(cls.db).query_db(query,data)
    if len(results) < 1:
      return False
    return cls(results[0])
  
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM trip;"
    results = connectToMySQL(cls.db).query_db(query)
    recipes = []
    for r in results:
      recipes.append(cls(r))
    return recipes
  
  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM trip WHERE trip.id = %(id)s;"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def update(cls,data):
    query = "UPDATE trip SET name=%(name)s, description = %(description)s;"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def insert(cls, data):
    query = "INSERT INTO trip_has_list (trip_id, list_id) VALUES( %(trip_id)s, %(list_id)s )"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def trip_list(cls,data):
    query = "SELECT * FROM trip JOIN trip_has_list on trip.id = trip_has_list.trip_id JOIN trip on trip.id = trip_has_list.trip_id WHERE id = %(id)s"
    return connectToMySQL(cls.db).query_db(query,data)

  @staticmethod
  def validate(trip):
    validate = True
    if len(trip['name']) > 20:
      flash('List name cannot be more than 20 characters long', 'name')
      validate = False
    return validate