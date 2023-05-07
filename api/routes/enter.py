from flask import Blueprint, request, jsonify
from api.models.users import User

enter_bp = Blueprint('enter_bp', __name__)

@enter_bp.route('/enter', methods=['POST'])
def enter():
  data = request.get_json()
  email = data.get('email')

  user = User.query.filter_by(email=email).first()

  if user:
    return jsonify({'status': '400', 'message': 'Email Found'})
  else: 
    return jsonify({'status': '404', 'message': 'Email Not Found'})