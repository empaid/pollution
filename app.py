from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
mongo_url = mongo_uri = "mongodb://admin:7pmiUS9mcOXUf96J@ac-gtzdkbl-shard-00-00.l6gtdgv.mongodb.net:27017,ac-gtzdkbl-shard-00-01.l6gtdgv.mongodb.net:27017,ac-gtzdkbl-shard-00-02.l6gtdgv.mongodb.net:27017/?ssl=true&replicaSet=atlas-11knd8-shard-0&authSource=admin&retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_url)
db = client.db

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes
from analytics import routes
@app.route('/')
def home():
  return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)