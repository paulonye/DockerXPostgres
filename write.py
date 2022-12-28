#!/usr/bin/env python3
import pandas as pd
import connect

data = pd.read_csv('test_data.csv')

print(data)

engine = connect.get_connection()

print('pushing data')
data.to_sql(name = 'datbase2', con = engine, if_exists = 'replace')
print('data has been pushed')

# print('Gettting Data')
# query = """SELECT * FROM datbase2"""
# df = pd.read_sql(query, con=engine)ß
# print(df)

engine.connect().close()
print('Done')