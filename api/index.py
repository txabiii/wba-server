from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Hello, World!'

@app.route('/about')
def about():
  return 'About'

@app.route('/test')
def test():
  return 'Testing'

if __name__ == '__main__':
  app.run(port=8000)