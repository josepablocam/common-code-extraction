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


# In[ ]:


time_data = pd.read_csv('../input/timesData.csv')
time_data[20:25]


# In[ ]:


id_count_by_region = time_data.groupby('country')['world_rank'].count()
id_count_by_region.sort_values(na_position='last', inplace=True, ascending=False)
id_count_by_region[:10]


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
id_count_by_region[:10].plot(kind='barh', rot=0, title='Universities by Region')

