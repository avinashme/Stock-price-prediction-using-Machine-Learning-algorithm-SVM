# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:52:40 2018

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




def call(): 
    global a
    global b
    global c
    global d
    global e
    global f
    global h
    global data
    global Open
    global High
    global Low
    global Close
    global Adj_Close
    global Volume
    global Day
    global Month
    global Year
    global year
    global month
    for day in range(1,31):
        opeen=predict(h,a,day,month,year)[0]
        high=predict(h,b,day,month,year)[0]
        low=predict(h,c,day,month,year)[0]
        close=predict(h,d,day,month,year)[0]
        adj_close=predict(h,e,day,month,year)[0]
        volume=predict(h,f,day,month,year)[0]
        Open.append(opeen)
        High.append(high)
        Low.append(low)
        Close.append(close)
        Adj_Close.append(adj_close)
        Volume.append(volume)
        Day.append(day)
        Month.append(month)
        Year.append(year)




def predict(x,y,day,month,year):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVR()
    clf.fit(x_train,y_train)
    new_data=np.array([[year,month,day]])
    new_data=new_data.reshape(1,-1)
    predict=clf.predict(new_data)
    return predict




def writ(k):
    with open(k, 'w') as csvfile:
        fieldnames = ['Open','High','Low','Close','Adj Close','Volume','Year','Month','Day']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0,len(Open)):
            writer.writerows([{'Open': Open[i],'High': High[i],'Low': Low[i],'Close': Close[i],'Adj Close': Adj_Close[i],'Volume': Volume[i],'Year': Year[i],'Month': Month[i],'Day': Day[i]}])
        print("Check CSV file For output")



def returns(l):
    data = pd.read_csv(l)
    data = data.dropna(how='any',axis=0)
    data['return'] = (data['Close'] - data['Open']) / data['Open'] * 100.0
    print(data['return'].tail(1))    



    
def reset():
    global a
    global b
    global c
    global d
    global e
    global f
    global h
    global data
    global Open
    global High
    global Low
    global Close
    global Adj_Close
    global Volume
    global Day
    global Month
    global Year
    global year
    global month
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

print("\n")
print("*************** AXIS BANK ***************")
data = pd.read_csv('AXISBANK.NS.csv')
process()
writ('Axis.csv')
print("TO know predicted values open Axis.csv")
print("Returns of month April for overall returns check submition.csv")
returns('Axis.csv')
reset()



print("\n")
print("*************** HCL ***************")
data = pd.read_csv('HCLTECH.NS.csv')
process()
writ('HCL.csv')
print("TO know predicted values open HCL.csv")
print("Returns of month April for overall returns check submition.csv")
returns('HCL.csv')
reset()



print("\n")
print("*************** HDFC BANK ***************")
data = pd.read_csv('HDFCBANK.NS.csv')
process()
writ('HDFC.csv')
print("TO know predicted values open HDFC.csv")
print("Returns of month April for overall returns check submition.csv")
returns('HDFC.csv')
reset()



print("\n")
print("*************** ICICI BANK ***************")
data = pd.read_csv('ICICIBANK.NS.csv')
process()
writ('ICICI.csv')
print("TO know predicted values open ICICI.csv")
print("Returns of month April for overall returns check submition.csv")
returns('ICICI.csv')
reset()



print("\n")
print("*************** INDUSINBK ***************")
data = pd.read_csv('INDUSINDBK.NS.csv')
process()
writ('INDUSIN.csv')
print("TO know predicted values open INDUSIN.csv")
print("Returns of month April for overall returns check submition.csv")
returns('INDUSIN.csv')
reset()



print("\n")
print("*************** INFY BANK ***************")
data = pd.read_csv('INFY.NS.csv')
process()
writ('INFY.csv')
print("TO know predicted values open INFY.csv")
print("Returns of month April for overall returns check submition.csv")
returns('INFY.csv')
reset()



print("\n")
print("*************** KOTAK BANK ***************")
data = pd.read_csv('KOTAKBANK.NS.csv')
process()
writ('KOTAK.csv')
print("TO know predicted values open KOTAK.csv")
print("Returns of month April for overall returns check submition.csv")
returns('KOTAK.csv')
reset()



print("\n")
print("*************** SBIN ***************")
data = pd.read_csv('SBIN.NS.csv')
process()
writ('SBIN.csv')
print("TO know predicted values open SBIN.csv")
print("Returns of month April for overall returns check submition.csv")
returns('SBIN.csv')
reset()



print("\n")
print("*************** TECHM ***************")
data = pd.read_csv('TECHM.NS.csv')
process()
writ('TECHM.csv')
print("TO know predicted values open TECHM.csv")
print("Returns of month April for overall returns check submition.csv")
returns('TECHM.csv')
reset()



print("\n")
print("*************** WIPRO ***************")
data = pd.read_csv('WIPRO.NS.csv')
process()
writ('WIPRO.csv')
print("TO know predicted values open WIPRO.csv")
print("Returns of month April for overall returns check submition.csv")
returns('WIPRO.csv')
reset()



print("\n")
print("*************** YES BANK ***************")
data = pd.read_csv('YESBANK.NS.csv')
process()
writ('YES.csv')
print("TO know predicted values open YES.csv")
print("Returns of month April for overall returns check submition.csv")
returns('YES.csv')
reset()