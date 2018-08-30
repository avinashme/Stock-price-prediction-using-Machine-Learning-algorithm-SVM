# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:45:30 2018

@author: SACHIN
"""
import csv
import numpy as np
from sklearn import preprocessing, cross_validation, svm
import pandas as pd

data=[]
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
h=[]

Open=[]
High=[]
Low=[]
Close=[]
Adj_Close=[]
Volume=[]
Day=[]
Month=[]
Year=[]
year=2018
month=5



def process():
    global a
    global b
    global c
    global d
    global e
    global f
    global h
    global data
    data.replace('null',-99999, inplace=True)
    data['Year']=[d.split('/')[2] for d in data.Date]
    data['Month']=[d.split('/')[0] for d in data.Date]
    data['Day']=[d.split('/')[1] for d in data.Date]
    data.drop(['Date'],1,inplace=True)
    data = data.dropna(how='any',axis=0)
    a=np.array(data['Open'])
    b=np.array(data['High'])
    c=np.array(data['Low'])
    d=np.array(data['Close'])
    e=np.array(data['Adj Close'])
    f=np.array(data['Volume'])
    h=np.array(data.drop(['Open','High','Low','Close','Adj Close','Volume'],1))
    call()

def predict(x,y,z):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=1)
    clf=svm.SVR()
    clf.fit(x_train,y_train)    
    new_data=np.array([[2018,5,z]])
    new_data=new_data.reshape(1,-1)    
    predict=clf.predict(new_data)
    return predict


def call(): 
    global a
    global b
    global c
    global d
    global e
    global f
    global h
    global data
    for i in range(1,31):
        opeen=predict(h,a,i)[0]
        high=predict(h,b,i)
        low=predict(h,c,i)
        close=predict(h,d,i)
        adj_close=predict(h,e,i)
        volume=predict(h,f,i)
        print("Stocks for date 2018-5-",i)
        print("Open ",opeen)
        print("High ",high)
        print("Low ",low)
        print("Close ",close)
        print("Adj Close ",adj_close)
        print("Volume ",volume)
        print("\n")
    
def reset():
    global a
    global b
    global c
    global d
    global e
    global f
    global h
    global data
    data=[]
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    h=[]

print("\n")
print("*************** AXIS BANK ***************")
data = pd.read_csv('AXISBANK.NS.csv')
process()
reset()



print("\n")
print("*************** HCL ***************")
data = pd.read_csv('HCLTECH.NS.csv')
process()
reset()



print("\n")
print("*************** HDFC BANK ***************")
data = pd.read_csv('HDFCBANK.NS.csv')
process()
reset()



print("\n")
print("*************** ICICI BANK ***************")
data = pd.read_csv('ICICIBANK.NS.csv')
process()
reset()



print("\n")
print("*************** INDUSINBK ***************")
data = pd.read_csv('INDUSINDBK.NS.csv')
process()
reset()



print("\n")
print("*************** INFY BANK ***************")
data = pd.read_csv('INFY.NS.csv')
process()
reset()



print("\n")
print("*************** KOTAK BANK ***************")
data = pd.read_csv('KOTAKBANK.NS.csv')
process()
reset()



print("\n")
print("*************** SBIN ***************")
data = pd.read_csv('SBIN.NS.csv')
process()
reset()



print("\n")
print("*************** TECHM ***************")
data = pd.read_csv('TECHM.NS.csv')
process()
reset()



print("\n")
print("*************** WIPRO ***************")
data = pd.read_csv('WIPRO.NS.csv')
process()
reset()



print("\n")
print("*************** YES BANK ***************")
data = pd.read_csv('YESBANK.NS.csv')
process()
reset()


