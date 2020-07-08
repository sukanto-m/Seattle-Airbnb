#!/usr/bin/env python
# coding: utf-8

# In[99]:


import time
import folium
import pandas as pd
import numpy as np
print("Done")


# In[100]:


df = pd.read_csv('clean_listings.csv',index_col=0)
df.head()


# In[101]:


df.columns


# In[102]:


df1 = df.loc[df['property_type'] == 'Apartment',
              ['country','neighbourhood_group_cleansed','zipcode','latitude','longitude']]
df1.head()


# In[103]:


df1.shape


# In[104]:


df2 = df1[:500]
df2.head()


# In[105]:


m = folium.Map(location=[47.6062,-122.3321], tiles = 'OpenStreetMap', zoom_start = 12)


# In[106]:


tic = time.time()
for i in range(0,len(df2)):
    folium.Marker([df2.iloc[i]['latitude'],df2.iloc[i]['longitude']],
                  popup=df2.iloc[i]['neighbourhood_group_cleansed']).add_to(m)
m.save('apartments_map.html')
toc = time.time() - tic
print("Time taken to generate this map is %s seconds."%(toc))


# In[109]:


df3 = df.loc[df['property_type'] == 'House',
              ['country','neighbourhood_group_cleansed','zipcode','latitude','longitude']]
df3.head()


# In[111]:


df3.shape


# In[112]:


df4 = df3[:500]
df4.head()


# In[108]:


m_1 = folium.Map(location=[47.6062,-122.3321], tiles = 'OpenStreetMap', zoom_start = 12)


# In[113]:


tic = time.time()
for i in range(0,len(df4)):
    folium.Marker([df4.iloc[i]['latitude'],df4.iloc[i]['longitude']],
                  popup=df4.iloc[i]['neighbourhood_group_cleansed']).add_to(m_1)
m_1.save('houses_map.html')
toc = time.time() - tic
print("Time taken to generate this map is %s seconds."%(toc))


# In[ ]:




