#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


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
print("The rank of a matrix is:",np.linalg.matrix_rank(matrix1))

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
print("The rank of a matrix is:",np.linalg.matrix_rank(matrix2))


# In[4]:


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
print("The determinant of a matrix is:",np.linalg.det(matrix1))

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
print("The determinant of a matrix is:",np.linalg.det(matrix2))


# In[6]:


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
print("The inverse of a matrix is:",np.linalg.inv(matrix1))

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
print("The inverse of a matrix is:",np.linalg.inv(matrix2))


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
w,v=np.linalg.eig(matrix1)
print("The eigen values of a matrix1 is:",w)
print("The eigen vectors of a matrix1 is:",v)

R2 = int(input("Enter the number of second rows:"))
C2 = int(input("Enter the number of second columns:"))


print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix2 = np.array(entries).reshape(R2, C2)
print(matrix2)
print("The inverse of a matrix is:",np.linalg.inv(matrix2))
w,v=np.linalg.eig(matrix2)
print("The eigen values of a matrix2 is:",w)
print("The eigen vectors of a matrix2 is:",v)


# In[ ]:




