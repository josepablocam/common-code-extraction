#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

# Read in the file (King's County housing prices) and summarize the information

df = pd.read_csv('../input/kc_house_data.csv')

df.info()


# In[ ]:


df.describe() # Look at a description of the features


# In[ ]:


df.columns # What are the features?


# In[ ]:


feat_null = [feat for feat in df.columns if df[feat].isnull().sum()!=0]
feat_null # No Null values 
# Delve deeper later


# In[ ]:




