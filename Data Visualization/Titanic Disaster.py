#!/usr/bin/env python
# coding: utf-8

# # Visualizing the Titanic Disaster

# ### Introduction:
# 
# This exercise is based on the titanic Disaster dataset avaiable at [Kaggle](https://www.kaggle.com/c/titanic).  
# To know more about the variables check [here](https://www.kaggle.com/c/titanic/data)
# 
# 
# ### Step 1. Import the necessary libraries

# In[31]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv)

# ### Step 3. Assign it to a variable titanic 

# In[16]:


titanic=pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv")
titanic


# ### Step 4. Set PassengerId as the index 

# In[17]:


titanic.set_index('PassengerId',inplace=True)


# In[18]:


titanic


# ### Step 5. Create a pie chart presenting the male/female proportion

# In[24]:


count=titanic['Sex'].value_counts()
colors = ['yellow', 'pink']
f, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(count.values.tolist(), labels=count.index.values.tolist(), colors=colors,startangle=360,
        autopct='%.1f%%')
ax1.set_title('Male/Female proportion')


# ### Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender

# In[33]:


#colors = {'male':'yellow', 'female':'orange'}
#ax2.scatter(titanic.Fare,titanic.Age,c=titanic['Sex'].iloc[:-1].apply(lambda x: colors[x]))
#ax2.set_xlabel('Fare')
#ax2.set_ylabel('Age')
#ax2.set_title('Fare paid and the Age')
sns.scatterplot(x=titanic['Age'], y=titanic['Fare'], hue=titanic['Sex'])


# ### Step 7. How many people survived?

# In[30]:


titanic['Survived'].sum()


# ### Step 8. Create a histogram with the Fare payed

# In[32]:


sns.histplot(titanic['Fare'],bins=10)


# ### BONUS: Create your own question and answer it.

# In[36]:


#find how many male and female survived
titanic.groupby('Sex').Survived.mean().plot(kind='bar')
print (titanic.groupby('Sex').Survived.value_counts())


# In[ ]:




