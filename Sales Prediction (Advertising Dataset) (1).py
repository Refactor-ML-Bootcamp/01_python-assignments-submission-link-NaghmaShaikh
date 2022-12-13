#!/usr/bin/env python
# coding: utf-8

# # Improting Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[14]:


advertising= pd.read_csv("C:\\Users\\Hp\Downloads\\advertising.csv",sep=",")


# In[16]:


advertising.head()


# In[17]:


advertising.head(10)


# In[18]:


advertising.tail(10)


# # Observation of Dataset 

# In[20]:


advertising.shape


# In[21]:


advertising.info()


# In[22]:


advertising.describe()


# In[23]:


print(len(advertising.columns))


# In[24]:


for i in advertising.columns:
    print(i)


# In[25]:


advertising["TV"].value_counts()


# In[26]:


advertising["Radio"].value_counts()


# In[27]:


advertising["Newspaper"].value_counts()


# In[40]:


advertising['Sales'].sum()


# # Data Cleaning

# In[51]:


#Checking for null values
advertising.isnull().sum()


# # EDA (Exploratory Data Analysis)

# In[33]:


#Scatter plot of target based on sales
x = advertising["Newspaper"]
y = advertising["Sales"]
plt.figure(figsize = (10,9))
plt.scatter(x ,y)
plt.xlabel("Newspaper")
plt.ylabel("Sales")


# In[81]:


sns.boxplot(data=advertising,y=advertising['Newspaper'])


# In[82]:


fig, axes = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(advertising['TV'], ax = axes[0])
plt2 = sns.boxplot(advertising['Newspaper'], ax = axes[1])
plt3 = sns.boxplot(advertising['Radio'], ax = axes[2])
plt.tight_layout()


# In[36]:


advertising.corr()


# In[54]:


# Correlation Heatmap to fine out highly correlated columns
plt.figure(figsize = (20,20))
sns.heatmap(advertising.corr(),annot = True,cmap="Reds",linewidths=2)


# In[41]:


sns.histplot(advertising['Sales'],bins=10)


# In[80]:


sns.histplot(advertising)


# In[53]:


plt.rcParams['figure.figsize']=(10,5)
sns.countplot(x=advertising.TV)
plt.show();


# In[49]:


sns.pairplot(advertising, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()


# In[78]:


sns.violinplot(data=advertising,y=advertising['TV'])


# In[79]:


advertising.plot(kind='box', title='boxplot')


# In[ ]:




