# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:24:12 2020
@author: Puruboii
"""
#pip install pandas
#pip install webbrowser
#pip install pyautogui
#pip install time
import pandas as pd
import webbrowser as web 
import time
import pyautogui as pg
import mysql.connector
pd.__version__
"""To extract data from database Mysql using connector"""
#establishing the connection
conn = mysql.connector.connect(
 user='root', password='********', host='127.0.0.1', database='database_name')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Retrieving single row
sql = '''SELECT * from Friends'''
#Executing the query
cursor.execute(sql)
#Fetching 1st row from the table
table = cursor.fetchall()
#using pandas to convert to dataframe format
df = pd.DataFrame(table, columns=['Fid','value 1', 'Phone number'])
df.info() # describes the table 
df.head() # gives 1st 5 rows
df.tail() # gives last 5 rows
bp_num = list(df['Phone number']) # takes phone number column stores in a list 
bp_value_1 = list(df['value 1']) # values can be anything with respect to 
message what is required to be pullled from table , here i hv taken names as valuesfor i in range(len(bp_num)+1):
 
web.open('https://web.whatsapp.com/send?phone='+'91'+str(bp_num[i])+'&text='+"Happy
Diwali, {} ".format(str(bp_value_1[i])))
width,height = pg.size()
pg.click(width/2,height/2)
time.sleep(5)
pg.press('enter')
time.sleep(3)
conn.close()
         
