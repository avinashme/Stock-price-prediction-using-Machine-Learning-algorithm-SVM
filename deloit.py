# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:02:23 2018

@author: SACHIN
"""

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



def predict(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVR()
    clf.fit(x_train,y_train)
    new_data=np.array([[2018,5,15]])
    new_data=new_data.reshape(1,-1)
    predict=clf.predict(new_data)
    return predict
    
for i in range(5,31):
    opeen=predict(h,a)
    high=predict(h,b)
    low=predict(h,c)
    close=predict(h,d)
    adj_close=predict(h,e)
    volume=predict(h,f)
    print("Stocks for date 2018-5-",i)
    print("Open ",opeen)
    print("High ",high)
    print("Low ",low)
    print("Close ",close)
    print("Adj Close ",adj_close)
    print("Volume ",volume)
    print("\n")
    
print(sum(d)-sum(a)/)