#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1


# importing pandas
import pandas as pd

# multi-list
list = [ ['Geeks'], ['For'], ['Geeks'], ['is'],
		['a'], ['portal'], ['for'], ['geeks'] ]
		
# create Pandas Series
df = pd.Series((i[0] for i in list))

print(df)


# In[3]:


#Q2

import pandas as pd

date_series = pd.date_range(start = '05-01-2021', end = '05-12-2021')

print(date_series)


# In[4]:


#Q3

# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
	'Name' : ['Akhila', 'Aishwarya', 'Vineetha', 'Anjali'],
	'Age' : [23, 21, 22, 21],
	'University' : ['KTU', 'KU', 'DU', 'BHU'],
}

# creating a Dataframe object
df = pd.DataFrame(details)

df


# In[9]:


#Q4

import pandas as pd
	
# List1
lst = [['Vineetha', 'Vijayan', 22], ['Aiswarya', 'Chandran', 21],
	['Anjali', 'Krishna', 23], ['Anju', 'Anil', 22]]
	
df = pd.DataFrame(lst, columns =['FName', 'LName', 'Age'],
										dtype = float)
print(df)


# In[12]:


#Q5

import pandas
emp_df = pandas.read_csv('read.csv')
print(emp_df)


# In[14]:


#Q6

#import libraries

import numpy as np
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'Name': ['Raj', 'Akhil', 'Sonum', 'Tilak', 'Divya', 'Megha'],
				'Age': [20, 22, 21, 19, 17, 23],
				'Rank': [1, np.nan, 8, 9, 4, np.nan]})

# printing the dataframe
print('DATAFRAME')
df


# In[16]:


#import libraries
import numpy as np
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'Name': ['Raj', 'Akhil', 'Sonum', 'Tilak', 'Divya', 'Megha'],
				'Age': [20, 22, 21, 19, 17, 23],
				'Rank': [1, np.nan, 8, 9, 4, np.nan]})


# using the sorting function
print('SORTED DATAFRAME')
df.sort_values(by=['Age'], ascending=False)


# In[17]:


#Q7

import pandas as pd
df = pd.DataFrame([[1,2,5],[4,5,6],[6,5,5]],columns=['a','b','c'])
df.set_index('a',inplace=True)
df


# In[18]:


df.reset_index(inplace=True)
df


# In[19]:


#Q8

import pandas as pd
df = pd.read_csv('Medal.csv')
df.head(2)


# In[20]:


#Q9

import pandas as pd
df = pd.DataFrame({'Name':['W','X','Y','Z'],
                  'Occupation':['ABC','ABC','PQR','PQR'],
                  'Salary':[100,120,80,86]})
df


# In[21]:


avg_sal = df.groupby('Occupation').mean()
avg_sal


# In[22]:


#Q10

import pandas as pd
df = pd.DataFrame({"Rollno":range(1,6),"Mark":[9,None,7,None,None]})
df


# In[23]:


df['Mark'].fillna(1,inplace=True)
df


# In[24]:


#q11

import pandas as pd
df = pd.DataFrame({'Company Name':['X','y','z'],
                   'Profit':[1,0,1]})
df


# In[25]:


df1=df['Profit']>0
df['Profit']=df1
df


# In[26]:


#Q12

import pandas as pd
df1 = pd.DataFrame({'eid':[1,2,3,4,5],
                   'ename':['V','W','X','Y','Z'],
                   'stipend':[100,101,102,103,104,]})
df2 = pd.DataFrame({'eid':[1,2,3,4,5],
                   'position':['ABC','PQR','ABC','PQR','ABC']})
df1


# In[30]:


import pandas as pd
df1 = pd.DataFrame({'eid':[1,2,3,4,5],
                   'ename':['V','W','X','Y','Z'],
                   'stipend':[100,101,102,103,104,]})
df2 = pd.DataFrame({'eid':[1,2,3,4,5],
                   'position':['ABC','PQR','ABC','PQR','ABC']})
df2


# In[31]:


df1.merge(df2)


# In[ ]:




