#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print((check_output(["ls", "../input"]).decode("utf8")))

# Any results you write to the current directory are saved as output.


# In[ ]:


df=pd.read_csv("../input/timesData.csv")


# In[ ]:


df.describe()


# In[ ]:


us=df.country=="United States of America"
au=df.country=="Australia"
ch=df.country=="China"
uk=df.country=="United Kingdom"
ca=df.country=="Canada"
ge=df.country=="Germany"


# In[ ]:


USA=df[us]
Australia=df[au]
China=df[ch]
United_Kingdom=df[uk]
Canada=df[ca]
Germany=df[ge]


# In[ ]:


new_df=USA.append([Australia,China,United_Kingdom,Canada,Germany])
new_df


# In[ ]:


country_name= ['USA', 'Australia', 'China', 'UK', 'Canada', 'Germany']
frequencies = [659,117,83,300,108,152]
pos = np.arange(len(country_name))
width = 0.7
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(country_name)
plt.bar(pos, frequencies, width, color='g')
plt.ylabel("Count")
plt.show()


# In[ ]:


USAI=USA.income.convert_objects(convert_numeric=True).dropna()
AustraliaI=Australia.income.convert_objects(convert_numeric=True).dropna()
ChinaI=China.income.convert_objects(convert_numeric=True).dropna()
United_KingdomI=United_Kingdom.income.convert_objects(convert_numeric=True).dropna()
CanadaI=Canada.income.convert_objects(convert_numeric=True).dropna()
GermanyI=Germany.income.convert_objects(convert_numeric=True).dropna()



# In[ ]:


plt.hist(USAI,bins=10)
plt.xticks([30,40,50,60,70,80,90,100])
plt.xlabel("USA Income")


# In[ ]:


plt.hist(AustraliaI,bins=10)
plt.xticks([30,40,50,60,70,80,90,100])
plt.xlabel("Australia Income")


# In[ ]:


plt.hist(ChinaI,bins=10)
plt.xticks([30,40,50,60,70,80,90,100])
plt.xlabel("China Income")


# In[ ]:


plt.hist(United_KingdomI,bins=10)
plt.xticks([30,40,50,60,70,80,90,100])
plt.xlabel("United Kingdom Income")


# In[ ]:


plt.hist(CanadaI,bins=10)
plt.xticks([30,40,50,60,70,80,90,100])
plt.xlabel("Canada Income")


# In[ ]:


plt.hist(GermanyI,bins=10)
plt.xticks([30,40,50,60,70,80,90,100])
plt.xlabel("Germany Income")


# In[ ]:


df["income"]=df["income"].replace("-",np.NaN)


# In[ ]:


#Lets make a heatmap to find out the correlations among the variables
corr=df.corr()
sns.heatmap(corr)


# In[ ]:


#The heat map says it all. We can see that teaching is positively correlated with research and citations 
#and it makes sense.
#research is positively correlated with citations
#There is some related between student_staff_ratio and year


# In[ ]:


#Lets plot them individually to get more insights
#Lets see how the teaching is related to the research
plt.scatter(df["teaching"],df["research"])
plt.xlabel("Teaching")
plt.ylabel("Research")


# In[ ]:


#Above graph shows that teaching and research are hihgly linearly corelated
plt.scatter(df["research"],df["citations"])
plt.xlabel("Teaching")
plt.ylabel("Citations")


# In[ ]:


#There is some correlation between teaching and Citations
plt.scatter(df["research"],df["citations"])
plt.xlabel("Research")
plt.ylabel("Citations")


# In[ ]:


#There is some correlation between Research and Citations
plt.scatter(df["year"],df["student_staff_ratio"])
plt.xlabel("Year")
plt.ylabel("Student_Staff_Ratio")


# In[ ]:


#lets see which country has the best teaching and research


# In[ ]:


sns.barplot("country","teaching",data=new_df)


# In[ ]:


sns.barplot("country","research",data=new_df)

