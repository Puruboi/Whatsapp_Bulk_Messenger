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
pd.__version__
path =r"**********************" # excel or csv file path 
df=pd.read_excel(path)
#df = pd.read_csv(path)
df.info() # describes the table 
df.head() # gives 1st 5 rows
df.tail() # gives last 5 rows
bp_num = list(df['Phone number']) # takes phone number column stores in a list 
bp_value_1 = list(df['value 1']) # values can be anything with respect to 
message what is required to be pullled from table , here i hv taken names as values
 
for i in range(len(bp_num)+1):
 
web.open('https://web.whatsapp.com/send?phone='+'91'+str(bp_num[i])+'&text='+"Happy
Diwali, {} ".format(str(bp_value_1[i])))
 width,height = pg.size()
 pg.click(width/2,height/2)
 time.sleep(5)
 pg.press('enter')
 time.sleep(3
