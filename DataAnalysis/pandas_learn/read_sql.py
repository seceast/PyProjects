# -*- coding: utf-8 -*-
# __author__ = yangyd 
# File: read_sql.py
# Create time: 2020/4/30 0030 10:20


import pandas as pd
from pandas_learn.database_connection import connect
import pymysql

cur = connect.cursor()


sql = 'SELECT * FROM users'

cur.execute(sql)
connect.commit()
sql_data = cur.fetchall()
print(sql_data)

df = pd.DataFrame(sql_data)
print(df)

# df = pd.read_sql(sql, connect)
# print(type(df))

