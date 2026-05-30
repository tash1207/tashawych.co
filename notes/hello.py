import pymongo

from bottle import get, post, redirect, request, run, static_file, template
from datetime import datetime

@get('/notes')
def notes():
  cursor = db.notes.find().sort([
    ('date', pymongo.DESCENDING)
  ])

  output = template('notes', cursor=cursor)
  return output

@get('/notes/add')
def get_notes_add():
  return '''
    <form action="/notes/add" method="post">
      Note: <input name="note" type="text" />
      <input value="Add" type="submit" />
    </form>
  '''

@post('/notes/add')
def post_notes_add():
  note = request.forms.get('note')
  db.notes.insert_one(
    {'note': note, 'date': datetime.now()}
  ) 
  redirect('/notes')

@get('/<filename>')
def server_static(filename):
  return static_file(filename, root='static/')

connection = pymongo.MongoClient()
db = connection.notes

run(host='0.0.0.0', port=8080)
