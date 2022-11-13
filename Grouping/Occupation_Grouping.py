#!/usr/bin/env python
# coding: utf-8

# # Occupation

# ### Introduction:
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import numpy as np
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# # Step 3. Assign it to a variable called users.
# 

# In[4]:


users=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", delimiter="|")
users.head()


# ### Step 4. Discover what is the mean age per occupation

# In[6]:


users.groupby('occupation')['age'].mean()


# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least

# In[7]:


users["gender_Male"]=users.gender.apply(lambda x: True if x=="M" else False)


(users.groupby("occupation")["gender_Male"].sum()/users.groupby("occupation")["gender_Male"].count()).sort_values(ascending=False)


# ### Step 6. For each occupation, calculate the minimum and maximum ages

# In[8]:


users.groupby("occupation")['age'].agg(["min","max"])


# ### Step 7. For each combination of occupation and gender, calculate the mean age

# In[12]:


users.groupby(["occupation","gender"])['age'].mean()


# ### Step 8.  For each occupation present the percentage of women and men

# In[14]:


users.groupby("occupation").gender.value_counts("M")*100


# In[ ]:




