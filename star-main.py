import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


def main():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("calc-416509-5e45d4492f28.json", scopes)
    file = gspread.authorize(credentials)
    sheet = file.open("ВВЛ")
    # sheet = sheet.sheet1
    worksheet1 = sheet.worksheet('Лист1')
    worksheet2 = sheet.worksheet('Лист2')
    # all_cells = sheet.range('B18:C18')
    all_cells = worksheet1.range('B18:C18')
    all_cells2 = worksheet2.range('I6:I43') + worksheet2.range('I46:I99')
    # print(list(map(lambda x: x.value, all_cells)))
    print(list(map(lambda x: x.value, all_cells2)))

if __name__ == '__main__':
    main()

