# this placeis for the database
import sqlite3

database = sqlite3.Connection('task.db' , check_same_thread=False)
query = database.cursor()

TABLE_NAME = "TASK"

def display_data(id):
  command = query.execute(f'Select * from {TABLE_NAME} where id={id}').fetchall()
  return command

def post_data(content , date):
  command = query.execute(f"INSERT INTO {TABLE_NAME} ('content' , 'Date_Created') VALUES (?,?)",(content , date))
  if command:
    database.commit()

def quering_by_date():
  command = query.execute(f"Select * from {TABLE_NAME} ORDER BY Date_Created").fetchall()  
  return command

def delete(id):
  try:
    if query.execute(f'DELETE FROM {TABLE_NAME} where id=(?)',(id,)):
      database.commit()
  except:
    print('there was a problem deleting your post')


def update_post(t_id , content):
  if query.execute(f'UPDATE {TABLE_NAME} SET content = (?) WHERE id=(?)' , (content,t_id)):
      database.commit()
