from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os 

from api.routes.demo import demo_bp
from api.routes.enter import enter_bp
from api.db import db


app = Flask(__name__)

app.config[
  "SQLALCHEMY_DATABASE_URI"
] = os.getenv('NEON_CONNECTION_STRING')

db.init_app(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) 

app.register_blueprint(demo_bp)
app.register_blueprint(enter_bp)


@app.route('/')
def home():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'About'

if __name__ == '__main__':
  app.run()