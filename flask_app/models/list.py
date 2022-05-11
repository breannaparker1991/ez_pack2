from flask import flash
from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class List:
  db = 'ez_pack'
  def __init__ (self, db_data):
    self.id = db_data['id']
    self.name = db_data['name']
    self.item = db_data['item']
    self.description = db_data['description']
    self.created_at = db_data['created_at']
    self.updated_at = db_data['updated_at']
    self.user_id = db_data['user_id']


  @classmethod
  def save(cls,data):
    query = "INSERT INTO list (name, description, item, user_id) VALUES ( %(name)s, %(description)s,%(item)s, %(user_id)s);"
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
    lists = []
    for r in results:
      lists.append(cls(r))
    return lists
  
  @classmethod
  def destroy(cls, data):
    query = "DELETE FROM list WHERE list.id = %(id)s;"
    return connectToMySQL(cls.db).query_db(query,data)
  
  @classmethod
  def update(cls,data):
    query = "UPDATE list SET name=%(name)s, description = %(description)s, item=%(item)s;"
    return connectToMySQL(cls.db).query_db(query,data)

  @staticmethod
  def validate(list):
    validate = True
    if len(list['name']) > 20:
      flash('List name cannot be more than 20 characters long', 'name')
      validate = False
    if len(list['description']) > 50:
      flash('List description cannot be more than 50 characters long', 'name')
      validate = False
    return validate