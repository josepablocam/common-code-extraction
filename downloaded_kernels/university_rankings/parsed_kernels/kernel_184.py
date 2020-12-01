#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd 

get_ipython().run_line_magic('matplotlib', 'inline')
pd.set_option('display.max_rows', 100)

df = pd.read_csv("../input/cwurData.csv")
df


# In[ ]:


#Tabeli read, mis käivad Eesti ülikoolide kohta

df[df["country"] == "Estonia"]


# In[ ]:


#keskmine hariduse kvaliteedi näitaja grupeerituna riikide kaupa
df.groupby(["country"])["quality_of_education"].mean()
#all on teise kujundusega tabel, eemaldage "#"
#df.groupby("country").aggregate({"quality_of_education": ["mean"]})


# In[ ]:


#Riikide keskmise hariduse kvaliteedi näitaja tulemuse järgi kahanevalt
a = df.groupby(["country"])["quality_of_education"].mean()
a.sort_values(ascending=False)


# In[ ]:


#Mitu korda iga riigi ülikoole tabelis esineb
koolid = df.groupby(["country"])["year"].count()
koolid.sort_values(ascending=False)


# In[ ]:


#Mitu korda iga riigi ülikoole tabelis esineb ainult 2015. aasta tulemuste kohta
a2015 = df[df["year"] == 2015]
koolid2015 = a2015.groupby(["country"])[("year")].count()
koolid2015.sort_values(ascending=False)

