#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,18])
ypoints = np.array([3,10,12,20])
plt.plot(xpoints,ypoints,marker='o',ls=':',c='red',mec='g',mfc='g')
plt.show()


# In[2]:


import matplotlib.pyplot as plt

x = [12,14,16,18,20,22,24]
y = [100,200,250,400,300,450,500]

plt.plot(x,y)
plt.xlabel('Temperature in degree Celsius')
plt.ylabel('Sales')
plt.show()


# In[5]:


import matplotlib.pyplot as plt
with open("Vineetha.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()


# In[ ]:




