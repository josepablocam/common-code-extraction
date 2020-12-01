#!/usr/bin/env python
# coding: utf-8

# Tried backward elimination with a significance level of 0.05. The perfrormance is same as though considering all the variables. 

# In[1]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print((check_output(["ls", "../input"]).decode("utf8")))

# Any results you write to the current directory are saved as output.


# In[7]:


dataset = pd.read_csv("../input/kc_house_data.csv",engine="python")


# In[9]:


dataset.columns


# In[20]:


# let's check P-value and remove the insignificant variables
# Initially let's take all variables.
x = dataset[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot','floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'sqft_living15', 'sqft_lot15']]

y = dataset['price']


# In[21]:


# statsmodel to do backward elimination
import statsmodels.formula.api as sm
regressor_OLS = sm.OLS(endog = y, exog = x).fit()
regressor_OLS.summary()


# In[14]:


#since floors has a value of more than .05 let's remove it
x = dataset[['bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot','waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'sqft_living15', 'sqft_lot15']]


# In[17]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, random_state=3)


# In[18]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)


# In[19]:


accuracy = regressor.score(x_test, y_test)
"Accuracy: {}%".format(int(round(accuracy * 100)))


# In[ ]:




