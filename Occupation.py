#!/usr/bin/env python
# coding: utf-8

# # Ex3 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[15]:


import numpy as np
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# In[17]:


Occup=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",delimiter="|").set_index("user_id")


# ### Step 4. See the first 25 entries

# In[18]:


Occup.head(25)


# ### Step 5. See the last 10 entries

# In[19]:


Occup.tail(10)


# ### Step 6. What is the number of observations in the dataset?

# In[21]:


Occup.shape


# In[22]:


print(len(Occup))


# ### Step 7. What is the number of columns in the dataset?

# In[23]:


print(len(Occup.columns))


# ### Step 8. Print the name of all the columns.

# In[24]:


print(Occup.columns)


# In[25]:


for i in Occup.columns:
    print(i)


# ### Step 9. How is the dataset indexed?

# In[26]:


Occup.index


# ### Step 10. What is the data type of each column?

# In[30]:


type(Occup.columns)
Occup.info()


# ### Step 11. Print only the occupation column

# In[31]:


Occup["occupation"]


# ### Step 12. How many different occupations are in this dataset?

# In[32]:


Occup["occupation"].nunique()


# ### Step 13. What is the most frequent occupation?

# In[34]:


Occup["occupation"].value_counts()


# ### Step 14. Summarize the DataFrame.

# In[35]:


Occup.info()


# ### Step 15. Summarize all the columns

# In[37]:


Occup.describe()


# ### Step 16. Summarize only the occupation column

# In[40]:


Occup["occupation"].describe()


# ### Step 17. What is the mean age of users?

# In[41]:


Occup["age"].mean()


# ### Step 18. What is the age with least occurrence?

# In[42]:


Occup["age"].value_counts()


# In[ ]:




