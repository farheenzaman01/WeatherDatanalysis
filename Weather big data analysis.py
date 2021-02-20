#!/usr/bin/env python
# coding: utf-8

# # ANANALYSIS BIG DATA ON WEATHER FORCAST
# 
# THE WEATHER IS A TIME SERIES DATA SET PER INFORMATION ABOUT WEATHER CONDITION AT A SPECIFIC REGION.THIS DATA SET RECORDS TEMPARATURE, DEW POINTS AND RELATIVE HUMIDITY, WIND SPEED, VISIBILITY, ACCOUNT AND CONDITIONS.
# 
# FOLOWING DATA SET WILL BE ANALYZED USING PANDAS DATA FRAME 

# In[5]:


import pandas as pd


# In[6]:


data = pd.read_csv(r"C:\Users\farhe\OneDrive\Documents\Bigdata\1. Weather Data.csv")


# In[7]:


data


# #    ANALYZING THE DATA USING .head() command
#  showing the first N rows in the data

# In[8]:


data.head()


# In[9]:


#.shape
shows the total number pf rows and columns


# In[ ]:


data.shape


# In[ ]:


#.index of dataframe


# In[ ]:


data.index


# In[ ]:


data.columns #displaying dataframe columns


# In[ ]:


#displaying datatypes
data.dtypes


# In[ ]:


# displaying unique values
data['Weather'].unique()


# In[ ]:


#.nunique displaying sum of unique values in each columns


# In[ ]:


data.nunique()


# In[ ]:


#displaying sum of non nul values
data.count()


# In[ ]:


#.value_counts()displaying unique values with their count
data['Weather'].value_counts()


# In[ ]:


#display basic information .info()
data.info()


# # DISPLAYING UNIQUE 'WIND SPEED' VALUE

# In[10]:


data.head(2)


# In[11]:


data.nunique()


# In[12]:


data['Wind Speed_km/h'].nunique()


# In[13]:


data['Wind Speed_km/h'].unique() #analysis


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




