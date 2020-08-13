import os
import smtplib
from email.message import EmailMessage
import gspread
import email_auth


gc = gspread.service_account(filename='google_auth.json')
sheet = gc.open('Scribble Collector')
worksheet = sheet.sheet1
total_scribble = len(worksheet.col_values(1))
total_sent = len(worksheet.col_values(8))

EMAIL_ADDRESS = email_auth.EMAIL_USER
EMAIL_PASSWORD = email_auth.EMAIL_PASS

def rowExtractor(row):  
    Row = worksheet.row_values(row)
    worksheet.update_cell(row,8, 'mailed')
    # print(Row)
    # print(len(Row))
    if len(Row) == 7 :
      # print('input Image available')
      val = Row[6].split("=")
      ImageUrl = 'https://drive.google.com/uc?id='+val[1]+'&export=download'
      # print(ImageUrl)
    else:
      # print('Image not available')
      ImageUrl = 'https://drive.google.com/uc?id=1oC6ASFi-dOue4l6yc2ADbcVcBX-cYtey&export=download'

    return [Row[2],Row[3],Row[4],Row[5],ImageUrl]
# Sender , Receiver,ReceiverMail, Message  = rowExtractor(8)


mail_sent = 0

while total_scribble-total_sent >0 :
  Sender , Receiver,ReceiverMail, Message , ImageUrl  = rowExtractor(total_sent+1)


  msg = EmailMessage()
  msg['Subject'] = 'Hey ! ' + Receiver + ', you have a new scribble'
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = ReceiverMail
  msg.set_content('You have a new scribble')

  msg.add_alternative("""\

  """ , subtype = 'html')

  with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
      smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

      smtp.send_message(msg)
  
  total_sent = total_sent +1
  mail_sent = mail_sent + 1


print('Total mail sent in this run: ' + str(mail_sent))


