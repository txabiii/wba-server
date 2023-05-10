from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os 

from api.routes.demo import demo_bp
from api.routes.enter import enter_bp
from api.routes.login import login_bp
from api.routes.sign_up import sign_up_bp
from api.routes.verify import verify_bp
from api.db import db

app = Flask(__name__)

app.config[
  "SQLALCHEMY_DATABASE_URI"
] = os.getenv('NEON_CONNECTION_STRING')
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

app.secret_key = os.getenv('SESSION_SECRET_KEY')

db.init_app(app)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) 

app.register_blueprint(demo_bp)
app.register_blueprint(enter_bp)
app.register_blueprint(login_bp)
app.register_blueprint(sign_up_bp)
app.register_blueprint(verify_bp)

@app.route('/')
def home():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'About'

if __name__ == '__main__':
  app.run()