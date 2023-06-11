import smtplib
import os
from email.mime.text import MIMEText

def send_email(recipient, code):
  body = "Welcome to WBA. This is your verification code: " + str(code)
  password = os.getenv('EMAIL_PASSWORD')

  msg = MIMEText(body)
  msg['Subject'] = "Verification code"
  msg['From'] = "assist.wba@gmail.com"
  msg['To'] = recipient

  smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp_server.login("assist.wba@gmail.com", password)
  smtp_server.sendmail("assist.wba@gmail.com", recipient, msg.as_string())
  smtp_server.quit()