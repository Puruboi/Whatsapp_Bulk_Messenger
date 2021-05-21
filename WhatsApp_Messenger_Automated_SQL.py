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



 
class  WA_Auto:
    
    def __init__(self):
        
        self.sendmsg()
    
    def getter(self):
        
        message=input("Enter the msg to send: ")
        #a=input("enter the file path: ")
        #path=os.path.normpath(a)
        return message


    def fetch_data(self):
        
        """To extract data from database Mysql using connector"""
        #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='*********', host='127.0.0.1', database='database_name')
        
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
        bp_num = list(df['PHONE NUMBER']) # takes phone number column stores in a list 
        bp_value_1 = list(df['Value1']) # values can be anything with respect to 
        return bp_num,bp_value_1


    def sendmsg(self):
        
        message=self.getter()
        bp_num,bp_value_1=self.fetch_data()
        for i in range(len(bp_num)):
            web.open('https://web.whatsapp.com/send?phone='+'91'+str(bp_num[i])+'&text='+ message+" {} ".format(str(bp_value_1[i])))
            width,height = pg.size()
            pg.click(width/2,height/2)
            time.sleep(7)
            pg.press('enter')
            time.sleep(5)
            
user_1=WA_Auto()