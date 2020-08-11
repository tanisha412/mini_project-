import gspread
gc = gspread.service_account(filename='google_auth.json')
sheet = gc.open('Scribble Collector')

worksheet = sheet.sheet1

values_list = worksheet.row_values(2)

print(values_list)