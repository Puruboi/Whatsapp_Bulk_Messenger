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
#pd.__version__


def fetch_data(path):
    # excel or csv file path 
    df=pd.read_excel(path)
    #df = pd.read_csv(path)
    #df.info() # describes the table 
    #df.head() # gives 1st 5 rows
    #df.tail() # gives last 5 rows
    bp_num = list(df['PHONE NUMBER']) # takes phone number column stores in a list 
    bp_value_1 = list(df['Value1']) # values can be anything with respect to 
    return bp_num,bp_value_1


#message what is required to be pullled from table , here i hv taken names as values


def sendmsg():
    path,message=getter()
    bp_num,bp_value_1=fetch_data(path)
    for i in range(len(bp_num)):
        web.open('https://web.whatsapp.com/send?phone='+'91'+str(bp_num[i])+'&text='+ message+" {} ".format(str(bp_value_1[i])))
        width,height = pg.size()
        pg.click(width/2,height/2)
        time.sleep(5)
        pg.press('enter')
        time.sleep(3)

def getter():
    message=input("Enter the msg to send: ")
    a=input("enter the file path: ")
    path=os.path.normpath(a)
    return path,message    


sendmsg()

