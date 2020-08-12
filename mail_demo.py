import os
import smtplib
from email.message import EmailMessage
import gspread
gc = gspread.service_account(filename='google_auth.json')
sheet = gc.open('Scribble Collector')
worksheet = sheet.sheet1
total_scribble = len(worksheet.col_values(1))
total_sent = len(worksheet.col_values(8))

EMAIL_ADDRESS = 'atilondiya@gmail.com'
EMAIL_PASSWORD = 'demvsmxxmpzoeinq'

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
  msg['Subject'] = 'Hey ! ' + Sender + ' you have a new scribble'
  msg['From'] = EMAIL_ADDRESS
  msg['To'] = ReceiverMail
  msg.set_content('this is plain text msg')

  msg.add_alternative("""\
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Card Recipe</title>
    <!-- Reset styles -->
    <link rel="stylesheet" href="https://unpkg.com/modern-css-reset/dist/reset.min.css" />
    <!-- Google Fonts Muli -->
    <link href="https://fonts.googleapis.com/css2?family=Muli:wght@300;400;700&display=swap" rel="stylesheet"> 
    <link rel="stylesheet" href="styles.css">
    <!-- Icons -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.14.0/css/all.css" integrity="sha384-HzLeBuhoNPvSl5KYnjx0BT+WB0QEEqLprO+NBkkk5gbc67FTaL7XIGa2w1L0Xbgc" crossorigin="anonymous">
  
    <style>
  .wrapper {
  min-height: 30vh;
  color: #000;
  font-family: 'Muli', sans-serif;
  font-size: 1rem;
  background-color: #F1E8E6;
  display: -ms-grid;
  display: grid;
  place-items: center;
}

.card {
  background-color: #fff;
  padding: 1em;
  border-radius: 1em;
  max-width: 768px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-shadow: 0px 17px 34px -20px #f55951;
          box-shadow: 0px 17px 34px -20px #f55951;
}

.card img {
  border-radius: 0.5em;
  -o-object-fit: cover;
     object-fit: cover;
  height: 250px;
  width: 200px;
}

.card__container {
  position: relative;
  -webkit-box-flex: 2;
      -ms-flex-positive: 2;
          flex-grow: 2;
  margin-left: 1.4em;
}

.card__title {
  font-size: 1.6rem;
  font-weight: 700;
  margin: 0.7em 0;
}

.card__text {
  font-size: 1rem;
  margin-bottom: 0.8em;
  margin-right: 5em;
  width: 33ch;
}

.fa-heart {
  position: absolute;
  top: 0;
  right: 0;
  padding: 0.6em;
  border: 1px solid #F1E8E6;
  border-radius: 100%;
}

.stars {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-pack: start;
      -ms-flex-pack: start;
          justify-content: flex-start;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.stars__text {
  font-size: 1rem;
  font-weight: 700;
  opacity: 0.5;
  margin-left: 0.5em;
}

/* Ratings */
.rating:not(:checked) > input {
  display: none;
}

#like:not(:checked) > label {
  cursor: pointer;
  float: right;
  width: 30px;
  height: 30px;
  display: block;
  color: rgba(233, 54, 40, 0.4);
  line-height: 33px;
  text-align: center;
}

#like:not(:checked) > label:hover,
#like:not(:checked) > label:hover ~ label {
  color: rgba(233, 54, 40, 0.6);
}

#like > input:checked + label:hover,
#like > input:checked + label:hover ~ label,
#like > input:checked ~ label:hover,
#like > input:checked ~ label:hover ~ label,
#like > label:hover ~ input:checked ~ label {
  color: rgba(233, 54, 40, 0.8);
}

#like > input:checked ~ label {
  color: #e93628;
}


    </style>
  
  
  </head>
    <body>
      <h1 style = "color:blue;">""" + Message + """</h1>
      <section class="wrapper">
        <div class="card">
            <figure>
                <img src='"""+ ImageUrl +"""'alt="salad">
            </figure>
            <div class="card__container">
                <i class="far fa-heart fa-lg"></i>
                <p class="card__title"> From : """ + Sender + """</p>
                <p class="card__text">""" + Message + """</p>
                <div class="stars" >
                    <div class="rating" id="like">
                        <!-- FIFTH HEART -->
                        <input type="radio" id="heart_5" name="like" value="5" />
                        <label for="heart_5" title="Five">&#10084;</label>
                        <!-- FOURTH HEART -->
                        <input type="radio" id="heart_4" name="like" value="4" />
                        <label for="heart_4" title="Four">&#10084;</label>
                        <!-- THIRD HEART -->
                        <input type="radio" id="heart_3" name="like" value="3" />
                        <label for="heart_3" title="Three">&#10084;</label>
                        <!-- SECOND HEART -->
                        <input type="radio" id="heart_2" name="like" value="2" />
                        <label for="heart_2" title="Two">&#10084;</label>
                        <!-- FIRST HEART -->
                        <input type="radio" id="heart_1" name="like" value="1" />
                    <label for="heart_1" title="One">&#10084;</label>
                    </div>
                    <p class="stars__text">14K</p>
                </div>
            </div>
        </div>
    </section>
    <body>
  <html>
  """ , subtype = 'html')

  with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
      smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)

      smtp.send_message(msg)
  
  total_sent = total_sent +1
  mail_sent = mail_sent + 1


print('Total mail sent in this run: ' + str(mail_sent))


