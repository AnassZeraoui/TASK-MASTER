from flask import Flask , request , render_template , redirect , url_for
from flask_cors import CORS
import datetime as dt
from db import post_data , quering_by_date , delete , update_post , display_data
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///task.db"


CORS(app)

# Database creation 
# We will work with the Sqlite3 

# making the first decorator 
@app.route('/' , methods=('GET','POST'))
def index():
  if request.method == "POST" : 
    # grab the content of the task 
    content = request.form.get('content')
    post_data(content=content,date=str(dt.datetime.utcnow().date()))
    return redirect(url_for('index'))
  else:
    tasks = quering_by_date()
    return render_template('index.html' , task = tasks)


@app.route('/delete/<int:id>' , methods=['GET' , 'POST'])
def delet(id):
  # grabing the id
  delete(id)
  return redirect(url_for('index'))

@app.route('/UPDATE/<int:id>' , methods=['GET' , 'POST'])
def update(id):
  if request.method == "POST":
    update_post(t_id=id , content=request.form['new_post'])
    return redirect(url_for('index'))
  else:
    data = display_data(id)
  return render_template('update.html' , task_info= data[0][1] , task_id=data[0][0] )


if __name__ == "__main__":
  app.run(debug=True)