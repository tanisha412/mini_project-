import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'HY LOVE'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'ghunawat.1@iitj.ac.in'
msg.set_content('HELLO ,Whats up?')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

    smtp.send_message(msg)