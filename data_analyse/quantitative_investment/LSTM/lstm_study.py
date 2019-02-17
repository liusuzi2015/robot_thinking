# !/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM,Dense
import matplotlib.pyplot as plt

# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt

from keras.models import load_model

# In[2]:


look_back = 40
forward_days = 10
num_periods = 20


#open the csv, chose company_N, where N = {A, B, C or D}
df = pd.read_csv('data/ibm.csv')
#set date as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
#keep only the 'Close' column
df = df['Close']

df.head()

# print(df)

# plt.figure(figsize = (15,10))
# plt.plot(df, label='ibm')
# plt.legend(loc='best')
# plt.show()


array = df.values.reshape(df.shape[0],1)
array[:5]


# In[7]:

from sklearn.preprocessing import MinMaxScaler
scl = MinMaxScaler()
array = scl.fit_transform(array)
array[:5]


division = len(array) - num_periods*forward_days

array_test = array[division-look_back:]
array_train = array[:division]

#Get the data and splits in input X and output Y, by spliting in `n` past days as input X 
#and `m` coming days as Y.
def processData(data, look_back, forward_days,jump=1):
    X,Y = [],[]
    for i in range(0,len(data) -look_back -forward_days +1, jump):
        X.append(data[i:(i+look_back)])
        Y.append(data[(i+look_back):(i+look_back+forward_days)])
    return np.array(X),np.array(Y)

X_test,y_test = processData(array_test,look_back,forward_days,forward_days)
y_test = np.array([list(a.ravel()) for a in y_test])

X,y = processData(array_train,look_back,forward_days)
y = np.array([list(a.ravel()) for a in y])


from sklearn.model_selection import train_test_split
X_train, X_validate, y_train, y_validate = train_test_split(X, y, test_size=0.20, random_state=42)


# In[11]:


print(X_train.shape)
print(X_validate.shape)
print(X_test.shape)
print(y_train.shape)
print(y_validate.shape)
print(y_test.shape)


#Optionaly, you can load a model
model = load_model('Trained/single-company/LSTM_compA_LB40_FD10_E50_F50_S30.h5')
