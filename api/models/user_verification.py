from api.db import db
from datetime import datetime, timedelta

class UserVerification(db.Model):
  __tablename__ = 'email_verification'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  token = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  expires_at = db.Column(db.DateTime, nullable=False)

  user = db.relationship('User', back_populates='email_verification')

  def __init__(self, user_id, token, expiration_hours=1):
    self.user_id = user_id
    self.token = token
    self.expires_at = datetime.utcnow() + timedelta(hours=expiration_hours)

  def is_expired(self):
    return datetime.utcnow() > self.expires_at