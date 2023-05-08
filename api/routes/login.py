from flask import Blueprint, request, jsonify
from api.models.users import User
import bleach

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  email = bleach.clean(data.get('email'))
  password = bleach.clean(data.get('password'))

  user = User.query.filter_by(email=email).first()

  print(email, password) # Debugging statement
  print(user.check_password(password))

  if user and user.check_password(password):
    return jsonify({'status': '200', 'message': 'Login successful'})
  else:
    return jsonify({'status': '401', 'message': 'Login failed'})