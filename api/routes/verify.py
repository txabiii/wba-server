from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from api.models.user_verification import UserVerification
from api.models.users import User
from api.verification import send_email
from api.db import db

import bleach
import random

verify_bp = Blueprint('verify_bp', __name__)

@verify_bp.route('/verify/send', methods=['POST'])
def verify():
  data = request.get_json()
  email = bleach.clean(data.get('email'))
  id = bleach.clean(data.get('id'))
  
  token = random.randint(100000, 999999)

  send_email(email, token)

  user_verification = UserVerification(id, token)
  db.session.add(user_verification)
  db.session.commit()

  return jsonify({'status': 200, 'message': 'Verification email sent'})

@verify_bp.route('/verify/token', methods=['POST'])
def verifyToken():
  data = request.get_json()
  input_token = bleach.clean(data.get('inputToken'))
  id = bleach.clean(data.get('id'))

  user_verification = UserVerification.query.filter(id=id).first()

  if input_token == user_verification.token:
    user = User.query.filter_by(id=id).first()
    user.verified = True
    db.session.commit()
    return jsonify({'status': 200, 'message': 'User is verified'})
  else:
    return jsonify({'status': 401, 'message': 'Invalid token'})
  

@verify_bp.route('/verify/check', methods=['POST'])
@jwt_required()
def checkVerification():
  current_user_id = get_jwt_identity()

  user = User.query.filter_by(id=current_user_id).first()

  print(user.verified)

  if user.verified == True:
    return jsonify({'status': 200, 'message': 'User is verified'})
  else: 
    return jsonify({'status': 401, 'message': 'User is not verified'})