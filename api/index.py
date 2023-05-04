from flask import Flask
from flask_cors import CORS
from routes.demo import demo_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}) 
app.register_blueprint(demo_bp)

@app.route('/')
def home():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'About'

if __name__ == '__main__':
  app.run(port=8000)