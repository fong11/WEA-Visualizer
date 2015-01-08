import gspread

#using burnash repo at https://github.com/burnash/gspread

# Login with your Google account
gc = gspread.login('ieacmusv@gmail.com', 'iea@cmusv')

worksheet = gc.open("Orchestrator").sheet1

values_list = worksheet.col_values(1)
alertrow = values_list.index("30") + 1

polygon = worksheet.acell("S"+str(alertrow)).value
print polygon
