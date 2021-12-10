#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Matrix operations (using vectorization)and transformations
#Write Python programtocreate two matrices (read values from user) and find the following
#1.Dot Product  2.Transpose  3.Trace  4.Rank  5.Determinant  6.Inverse  7.Eigen values and eigen vectors
import numpy as np

R1 = int(input("Enter the number of first rows:"))
C1 = int(input("Enter the number of first columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix = np.array(entries).reshape(R1, C1)
print(matrix)

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix = np.array(entries).reshape(R2, C2)
print(matrix)


# In[ ]:





# In[5]:


import numpy as np

R1 = int(input("Enter the number of first rows:"))
C1 = int(input("Enter the number of first columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix1 = np.array(entries).reshape(R1, C1)
print(matrix1)

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
if(R1==C2):
    matrix3=np.dot(matrix1,matrix2)
    print(matrix3)


# In[7]:


import numpy as np

R1 = int(input("Enter the number of first rows:"))
C1 = int(input("Enter the number of first columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix1 = np.array(entries).reshape(R1, C1)
print(matrix1)

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
transpose_1 = np.transpose(matrix1)
print(transpose_1)
transpose_2 = np.transpose(matrix2)
print(transpose_2)


# In[9]:


import numpy as np

R1 = int(input("Enter the number of first rows:"))
C1 = int(input("Enter the number of first columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix1 = np.array(entries).reshape(R1, C1)
print(matrix1)

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
trace_1 = np.trace(matrix1)
print(trace_1)
trace_2 = np.trace(matrix2)
print(trace_2)


# In[ ]:




