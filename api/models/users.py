from api.db import db

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  verified = db.Column(db.Boolean, nullable=False, default=False)

  email_verification = db.relationship('UserVerification', backref='user_obj', uselist=False)

  def __init__(self, email, password):
    self.email = email
    self.password = password

  def __repr__(self):
    return f'<User {self.email}>'
  
  def check_password(self, password):
    print(str(self.password) + ' - ' + str(password))
    return (self.password == password)