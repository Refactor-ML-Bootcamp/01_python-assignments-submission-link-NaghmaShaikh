#!/usr/bin/env python
# coding: utf-8

# # MPG Cars

# ### Introduction:
# 
# The following exercise utilizes data from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Auto+MPG)
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import numpy as np
import pandas as pd


# ### Step 2. Import the first dataset [cars1](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv) and [cars2](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv).  

# In[2]:


cars1=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv")
cars1


# In[ ]:





#    ### Step 3. Assign each to a variable called cars1 and cars2

# In[4]:


cars2=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv")
cars2


# ### Step 4. Oops, it seems our first dataset has some unnamed blank columns, fix cars1

# In[5]:


cars1.dropna(axis=1,inplace=True)


# ### Step 5. What is the number of observations in each dataset?

# In[6]:


cars1.shape


# In[7]:


cars2.info


# In[8]:


cars1.describe


# ### Step 6. Join cars1 and cars2 into a single DataFrame called cars

# In[13]:


cars=pd.merge(cars1,cars2,how='outer')

cars


# ### Step 7. Oops, there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.

# In[17]:


owners = np.random.randint(15000,73000,398)
df = pd.DataFrame(owners, columns = ['owners'])
df


# ### Step 8. Add the column owners to cars

# In[18]:


cars = cars.join(df)
cars


# In[ ]:




