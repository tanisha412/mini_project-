
def rowExtractor(row):
    import gspread
    gc = gspread.service_account(filename='google_auth.json')
    sheet = gc.open('Scribble Collector')
    worksheet = sheet.sheet1
    Row = worksheet.row_values(row)
    # worksheet.update(row, 'Bingo!')
    return [Row[2],Row[3],Row[4]]

Sender , Receiver, Message  = rowExtractor(3)







