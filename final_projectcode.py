#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[16]:


# Reading dataset of globalsuperstore
df = pd.read_csv('Iris.csv')
df.head()


# In[17]:


# to delete the column ie Id
df = df.drop(columns=['Id'])
df.head()


# In[18]:


# to display statistics about data
df.describe()


# In[19]:


# to display basic info about datatype
df.info()


# In[23]:


# to display no of sample on each class
df['Species'].value_counts()


# In[25]:


#chech for null values
df.isnull().sum()


# In[56]:


#Histograms
df['SepalLengthCm'].hist()
plt.savefig('histogram')
plt.show()


# In[29]:


df['SepalWidthCm'].hist()


# In[31]:


#Scatterplot
colors = ['red','orange','blue']
Species = ['Iris-setosa', 'Iris-versicolor','Iris-virginica']


# In[50]:


for i in range(3):
    x = df[df['Species']== Species[i]]
    plt.scatter(x['SepalLengthCm'], x['SepalWidthCm'], c = colors[i], label = Species[i])

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()


# In[44]:


x = df['SepalLengthCm']
y = df['SepalLengthCm']

#Bar Graph
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.bar(x,y)


# In[42]:


plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.plot(x,y)


# In[ ]:




