# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:11:24 2018

@author: SACHIN
"""

import csv
import numpy as np
from sklearn import preprocessing, cross_validation, svm
import pandas as pd

data = pd.read_csv('AXISBANK.NS.csv')
data.replace('null',-99999, inplace=True)
data['Year']=[d.split('/')[2] for d in data.Date]
data['Month']=[d.split('/')[0] for d in data.Date]
data['Day']=[d.split('/')[1] for d in data.Date]
data.drop(['Date'],1,inplace=True)
a=np.array(data['Open'])
b=np.array(data['High'])
c=np.array(data['Low'])
d=np.array(data['Close'])
e=np.array(data['Adj Close'])
f=np.array(data['Volume'])
h=np.array(data.drop(['Open','High','Low','Close','Adj Close','Volume'],1))

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


def predict(x,y,day,month,year):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVR()
    clf.fit(x_train,y_train)
    new_data=np.array([[year,month,day]])
    new_data=new_data.reshape(1,-1)
    predict=clf.predict(new_data)
    return predict

    
for day in range(5,31):
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

with open('fdcg.csv', 'w') as csvfile:
    fieldnames = ['Open','High','Low','Close','Adj Close','Volume','Year','Month','Day']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0,len(Open)):
        writer.writerows([{'Open': Open[i],'High': High[i],'Low': Low[i],'Close': Close[i],'Adj Close': Adj_Close[i],'Volume': Volume[i],'Year': Year[i],'Month': Month[i],'Day': Day[i]}])
    print("Check CSV file For output")