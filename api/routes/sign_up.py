from flask import Blueprint, request, jsonify, session
import bleach
import hashlib

from api.db import db
from api.models.users import User

sign_up_bp = Blueprint('sign_up_bp', __name__)

@sign_up_bp.route('/sign-up', methods=['POST'])
def sign_up():  
  data = request.get_json()
  email = bleach.clean(data.get('email'))
  password = bleach.clean(data.get('password'))

  hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

  new_user = User(email=email, password=hashed_password)
  db.session.add(new_user)
  db.session.commit()

  session['user_id'] = new_user.id
  session['user_email'] = new_user.email

  return jsonify({'status': 200, 'message': 'User created successfully'})