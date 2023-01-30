import pandas as pd
from sqlalchemy import create_engine
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from connect import get_connection
from dotenv import load_dotenv
load_dotenv()

scope_app = ['https://www.googleapis.com/auth/drive',
             'https://spreadsheets.google.com/feeds']

def sheet_connection(sheetname, worksheet):

    key_file = os.getenv('key_file')

    cred = ServiceAccountCredentials.from_json_keyfile_name(
        key_file, scope_app
    )

    client = gspread.authorize(cred)

    sheet = client.open(sheetname)

    df = pd.DataFrame.from_dict(sheet.worksheet(worksheet).get_all_records())

    return df


def batch_records(sheetname, worksheet):

    df = sheet_connection(sheetname, worksheet)

    print(df.head(10))

    engine = get_connection()

    df.to_sql(name = 'yahoofinance', con = engine, if_exists = 'replace')

    engine.connect().close()


if __name__ == '__main__':
    batch_records('test_sheet', 'data')

