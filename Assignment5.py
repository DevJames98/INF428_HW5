#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#Open data
fileName='/Users/Devon/Google Drive/MyINF428/data/MachineLearning/indians-diabetes.csv'
diabetesData=pd.read_csv(fileName)


# In[4]:


diabetesData.head()


# In[21]:


diabetesData['class'].head()


# In[22]:


class0 = diabetesData[diabetesData['class']==0]
class1 = diabetesData[diabetesData['class']==1]


# In[23]:


#Make Scatter Plot

a = diabetesData.Glucose
b = diabetesData.bmi

plt.scatter(class0.Glucose,class0.bmi, color = "r")
plt.scatter(class1.Glucose,class1.bmi, color = "g")

plt.title('Scatter Chart using Glucose and BMI')
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.show()


# In[ ]:




