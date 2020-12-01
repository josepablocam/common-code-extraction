
# coding: utf-8

# #das_loans

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import seaborn as sns
import pandas as pd
df = pd.read_csv("../input/loan.csv", low_memory=False)


# In[ ]:


df.head(10)


# In[ ]:


df[4:]


# In[ ]:


df.describe()


# In[ ]:


df['funded_amnt'].value_counts()


# In[ ]:


df['loan_amnt'].hist(bins=10)


# In[ ]:


df['int_rate'].hist(bins=50)
# seems like most are concentrated between 10% - 15% interested rates


# In[ ]:


df.boxplot(column='int_rate')
# I suspected right


# In[ ]:


df.boxplot(column='int_rate', by = 'term')
#idk what this will do just curious I guess, will check if there is a sex or education level bias.


# In[ ]:


df.boxplot(column='loan_amnt')


# In[ ]:


df.boxplot(column='loan_amnt', by = 'term')


# In[ ]:


df.apply(lambda x: sum(x.isnull()),axis=0)
# I feel good getting around to this shit.
## I need to find all of the missing values in the dataset


# In[ ]:


Since I am using loan_amnt I need to do something about the missing values, I think the standard is to mean that ish


# In[ ]:


df['loan_amnt'].fillna(df['loan_amnt'].mean(), inplace=True)


# In[ ]:


df[-20:]


# In[ ]:


df['grade'].unique

