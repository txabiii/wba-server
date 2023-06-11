from flask import Flask
from flask_cors import CORS

from api.routes.demo import demo_bp

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://scrollarium.vercel.app"]}}) 

app.register_blueprint(demo_bp)

@app.route('/')
def home():
  return 'This is a Flask server'

if __name__ == '__main__':
  app.run()