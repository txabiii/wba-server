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
@jwt_required()
def verify():
  current_user_id = get_jwt_identity()

  user = User.query.filter_by(id=current_user_id).first()
  
  token = random.randint(100000, 999999)

  send_email(user.email, token)

  user_verification = UserVerification(user.id, token)
  db.session.add(user_verification)
  db.session.commit()

  return jsonify({'status': 200, 'message': 'Verification email sent'})

@verify_bp.route('/verify/token', methods=['POST'])
@jwt_required()
def verifyToken():
  data = request.get_json()
  input_token = bleach.clean(data.get('input_token'))

  current_user_id = get_jwt_identity()

  user_verification = UserVerification.query.filter_by(user_id=current_user_id).first()

  if input_token == user_verification.token:
    user = User.query.filter_by(id=current_user_id).first()
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

  if user.verified == True:
    return jsonify({'status': 200, 'message': 'User is verified'})
  else: 
    return jsonify({'status': 401, 'message': 'User is not verified'})