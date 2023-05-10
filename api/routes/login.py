from flask import Blueprint, request, jsonify, session
from flask_jwt_extended import create_access_token
import bleach
import hashlib

from api.models.users import User

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  email = bleach.clean(data.get('email'))
  password = bleach.clean(data.get('password'))

  user = User.query.filter_by(email=email).first()

  hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

  if user and user.check_password(hashed_password):
    access_token = create_access_token(identity=user.id, expires_delta=False)
    response = jsonify({'status': 200, 'message': 'Login successful', 'wba_access_token': access_token})
    return response
  else:
    return jsonify({'status': 401, 'message': 'Login failed'})