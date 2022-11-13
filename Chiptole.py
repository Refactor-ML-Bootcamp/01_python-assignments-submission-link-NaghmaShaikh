#!/usr/bin/env python
# coding: utf-8

# # Ex2 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import numpy as np
import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# In[4]:


chipo=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv",delimiter="\t")


# ### Step 3. Assign it to a variable called chipo.

# In[ ]:





# ### Step 4. See the first 10 entries

# In[5]:


chipo.head(10)


# In[15]:


chipo.info()


# In[16]:


chipo.describe()


# ### Step 5. What is the number of observations in the dataset?

# In[ ]:





# In[7]:


# Solution 1

print(len(chipo))


# In[8]:


# Solution 2
chipo.shape


# ### Step 6. What is the number of columns in the dataset?

# In[9]:


print(len(chipo.columns))


# ### Step 7. Print the name of all the columns.

# In[10]:


print(chipo.columns)


# ### Step 8. How is the dataset indexed?

# In[14]:


chipo.index


# In[17]:


a = chipo.head()
a


# ### Step 9. Which was the most-ordered item? 

# In[18]:


chipo['item_name'].value_counts()


# ### Step 10. For the most-ordered item, how many items were ordered?

# In[23]:


chipo['item_name'].value_counts()["Chicken Bowl"]


# ### Step 11. What was the most ordered item in the choice_description column?

# In[24]:


chipo['choice_description'].value_counts()


# ### Step 12. How many items were orderd in total?

# In[19]:


chipo['quantity'].sum()


# ### Step 13. Turn the item price into a float

# #### Step 13.a. Check the item price type

# In[26]:


type(chipo["item_price"])


# #### Step 13.b. Create a lambda function and change the type of item price

# In[35]:



chipo['item_price']= chipo['item_price'].map(lambda x :float(x))
chipo['item_price'].dtype


# #### Step 13.c. Check the item price type

# In[29]:


chipo.info()


# ### Step 14. How much was the revenue for the period in the dataset?

# In[38]:


#quantity * price
chipo["Revenue"]=chipo["quantity"]*chipo["item_price"]
x=chipo["Revenue"].sum()
print(x)


# ### Step 15. How many orders were made in the period?

# In[39]:


print(len(chipo["order_id"]))


# ### Step 16. What is the average revenue amount per order?

# In[42]:


# Solution 1
chipo["Revenue"].mean()
chipo["Revenue"].median()


# In[40]:


# Solution 2

avg_revenue=x/len(chipo["Revenue"])
avg_revenue


# ### Step 17. How many different items are sold?

# In[37]:


chipo['item_name'].nunique()


# In[ ]:




