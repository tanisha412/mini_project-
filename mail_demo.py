import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'tanighunawat412@gmail.com'
EMAIL_PASSWORD = 'rlwxrhuvgciwebdh'

def rowExtractor(row):
    import gspread
    gc = gspread.service_account(filename='google_auth.json')
    sheet = gc.open('Scribble Collector')
    worksheet = sheet.sheet1
    Row = worksheet.row_values(row)
    worksheet.update_cell(row,7, 'Bingo!')
    return [Row[2],Row[3],Row[4],Row[5]]

Sender , Receiver,ReceiverMail, Message  = rowExtractor(10)

msg = EmailMessage()
msg['Subject'] = 'Hey !' + Sender + 'you have a new scribble'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ReceiverMail
msg.set_content('this is plain text msg')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
  <body>
    <h1 style = "color:blue;">""" + Message + """</h1>
   <body>
<html>
""" , subtype = 'html')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

    smtp.send_message(msg)