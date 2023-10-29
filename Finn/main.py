import gspread

sa = gspread.service_account("credentials.json")
sh = sa.open("gspread test")

wks = sh.worksheet("Sheet1")

print('Rows: ', wks.row_count)
print('Cols: ', wks.col_count)

print(wks.acell('A1').value)
print(wks.cell(1, 2).value)
print(wks.get('A1:B2'))

    #print(wks.get_all_records())
    #print(wks.get_all_values())

wks.update('A3', 'POO')
wks.update('D2:E3', [['Engineering', 'Tennis'], ['Business', 'Pottery']])
wks.update('F2', '=UPPER(E2)', raw=False)

wks.delete_rows(9, 10)
