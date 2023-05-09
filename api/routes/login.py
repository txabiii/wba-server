from flask import Blueprint, request, jsonify, session
from api.models.users import User
import bleach
import hashlib

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  email = bleach.clean(data.get('email'))
  password = bleach.clean(data.get('password'))

  user = User.query.filter_by(email=email).first()

  hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

  if user and user.check_password(hashed_password):
    session['user_id'] = user.id
    session['user_email'] = user.email
    return jsonify({'status': 200, 'message': 'Login successful'})
  else:
    return jsonify({'status': 401, 'message': 'Login failed'})