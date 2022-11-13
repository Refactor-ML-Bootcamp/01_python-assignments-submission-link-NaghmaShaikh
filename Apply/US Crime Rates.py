#!/usr/bin/env python
# coding: utf-8

# # United States - Crime Rates - 1960 - 2014

# ### Introduction:
# 
# This time you will create a data 
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[9]:


import numpy as np
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv). 

# ### Step 3. Assign it to a variable called crime.

# In[10]:


crime=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv")


# In[11]:


crime.head()


# ### Step 4. What is the type of the columns?

# In[12]:


crime.info()


# ##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# 
# ### Step 5. Convert the type of the column Year to datetime64

# In[14]:


#crime['Year']=pd.to_datetime(crime['Year'],format='%Y')
crime['Year'] = pd.to_datetime(crime['Year'],format='%Y') 


# In[15]:


crime.info()


# ### Step 6. Set the Year column as the index of the dataframe

# In[16]:


crime.set_index("Year")


# ### Step 7. Delete the Total column

# In[17]:


crime.drop(columns=["Total"],inplace=True)
crime.head(2)


# ### Step 8. Group the year by decades and sum the values
# 
# #### Pay attention to the Population column number, summing this column is a mistake

# In[ ]:





# ### Step 9. What is the most dangerous decade to live in the US?

# In[18]:


crime.idxmax(0)


# In[ ]:




