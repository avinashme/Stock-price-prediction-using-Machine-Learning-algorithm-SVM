# -*- coding: utf-8 -*-
"""
Created on Sun May 13 19:57:53 2018

@author: SACHIN
"""

import numpy as np
from sklearn import preprocessing, cross_validation, svm
import pandas as pd
import datetime

data = pd.read_csv('AXISBANK.NS.csv')
data.replace('null',-99999, inplace=True)
#data.drop(['Date'],1,inplace=True)


data['Year']=[d.split('/')[2] for d in data.Date]
data['Month']=[d.split('/')[1] for d in data.Date]
data['Day']=[d.split('/')[0] for d in data.Date]



print(data[''])