
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'tanighunawat412@gmail.com'
EMAIL_PASSWORD = 'rlwxrhuvgciwebdh'

msg = EmailMessage()
msg['Subject'] = 'HY '
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'atilondiya@gmail.com'
msg.set_content('this is plain text msg')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
  <body>
    <h1 style = "color:blue;"> This is an HTML email </h1>
   <body>
<html>
""" , subtype = 'html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

    smtp.send_message(msg)