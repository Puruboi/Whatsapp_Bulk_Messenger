# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:39:14 2020
@author: Puruboi
"""
#pip install pandas
#pip install webbrowser
#pip install pyautogui
#pip install time
import pandas as pd
import webbrowser as web 
import time
import pyautogui as pg
import os
import datetime as dt
#pd.__version__



class  WA_Auto:
    
    def __init__(self):
        try:
            self.sendmsg()
        except Exception as e:
            print(e)
    
    def getter(self):
        try:
            message=input("Enter the msg to send: ")
            a=input("enter the file path: ")
            path=os.path.normpath(a)
            return path,message
        except Exception as e:
            print("Entered input is Invalid")
            print(e)


    def fetch_data(self,path):
        try:
            # excel or csv file path 
            df=pd.read_excel(path)
            #df = pd.read_csv(path)
            #df.info() # describes the table 
            #df.head() # gives 1st 5 rows
            #df.tail() # gives last 5 rows
            bp_num = list(df['PHONE NUMBER']) # takes phone number column stores in a list 
            bp_value_1 = list(df['Value1']) # values can be anything with respect to 
            return bp_num,bp_value_1
        
        except Exception as e:
            print("Enter path is wrong check the file path")
            print(e)
            
    def greet(self):
        
        try:
            h=dt.datetime.now().hour
            
            if h>=6 and h<=12:
                print("Good Morning...")
            if h>=13 and h<=16:
                print("Good Afternoon")
            if h>=17 and h<=20:
                print("Good Evening")
            if h>=21:
                print("Welcome During Nightime")
                
            print("Make sure your phone and pc is connected to strong internet connectivity")
            print("Make sure Atleast once u hv  logined  through whatsapp web atleast once in ur broswer or open whatsapp web in your phone to scan immediately ")
        except Exception as e:
            print(e)

############### message what is required to be pullled from table , here i hv taken names as values ##############


    def sendmsg(self):
        try:
            self.greet()
            path,message=self.getter()
            bp_num,bp_value_1=self.fetch_data(path)
            for i in range(len(bp_num)):
                web.open('https://web.whatsapp.com/send?phone='+'91'+str(bp_num[i])+'&text='+ message+" {} ".format(str(bp_value_1[i])))
                width,height = pg.size()
                pg.click(width/2,height/2)
                time.sleep(10)
                pg.press('enter')
                time.sleep(3)
        except Exception as e:
            print(e)
            print(" or may be internet issue ............")
        #finally:
            #print("Task Over")
            
 


user_1=WA_Auto()

