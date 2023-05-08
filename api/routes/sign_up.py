from flask import Blueprint, request, jsonify
from api.models.users import User
import bleach
from api.db import db

sign_up_bp = Blueprint('sign_up_bp', __name__)

@sign_up_bp.route('/sign-up', methods=['POST'])
def sign_up():  
  data = request.get_json()
  email = bleach.clean(data.get('email'))
  password = bleach.clean(data.get('password'))

  new_user = User(email=email, password=password)
  db.session.add(new_user)
  db.session.commit()

  return jsonify({'status': '200', 'message': 'User created successfully'})