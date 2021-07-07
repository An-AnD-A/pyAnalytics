# NumPy Tutorial

import numpy as np

# making an array

lst1 = [1.0,2.5,3.6]
lst2 = [3.5,6.5,7.8]
Ar1 = np.array([lst1,lst2])

print(Ar1)

# Get Dimensions and size

Ar1.ndim

print(type(Ar1.shape)) 

Ar1.dtype 

Ar1.itemsize 

# Specifying the size while maing an array.

Ar2 = np.array([1 , 2, 3], dtype = 'int16') # default would have been int32

Ar2.dtype 

Ar2.itemsize   #gives the size of the byte used.

# Get the total size

Ar2.size # gives the total number of elements

total_size = Ar2.size*Ar2.itemsize

print(total_size)

Ar2.nbytes  # second way to get total size.

# Getting Specific elements
 
Ar = np.array([[2,3,6,3,8,5,9,4],[4,7,2,5,9,2,6,1]], dtype = 'int32')
 
print(Ar)
 
# Getting one element based on index

Ar[1,4] 

# Getting a row or a column

Ar[0,:]

Ar[:,4]
 
# Getting a sequence of elements (parsing)

Ar[:,2:6]

# Using stepsize.

Ar[0,1:6:2]   # Ar[row index, column start:Column_end:step]

# changing an element.

print(Ar)

Ar[0,4] = 20

print(Ar)

# changing a sequence in row and column.

Ar[0,0:4] = 5

print(Ar)

Ar[0,0:4] = [ 3,4,5,6]

print(Ar)

# working with a 3d array.

Ar_3d = np.array([[[1,2],[2,1]], [[2,1],[1,2]]])

print(Ar_3d)

# get a specific element in  3d array.

Ar_3d [1,0,1]

# replace an elements in 3d array

Ar_3d[1,:,:] = [[3,3],[3,3]]

print(Ar_3d)

## Initializing different types of arrays

# All 0s matrix and 1s matrix. specifi dtype too.

Ar_3 = np.ones([4,3])
print(Ar_3)

Ar_4 = np.zeros([4,3])
print(Ar_4)

# make an identity matrix

Ar_5 = np.identity(4)
print(Ar_5)

#  matrix made of one scalar value

print(np.full([3,3],5))

# using full_like and full 

print(np.full_like(Ar_3d,5))

print(np.full(Ar_3d.shape,5))
# random integer and decimal numbers matrix. using random_sample

print(np.random.rand(2,5,5))

print(np.random.randint(5,10,[2,5,5]))  # randint(start,end,size)

print(np.random.random_sample([2,5,5])) # gives a random float between 0.0 to 1.0

# repeat array test with axis

print(np.repeat([[[1,2],[3,4]],[[5,6],[7,8]]],[2,2],axis = 2))

# axis order - z,y,x - 0,1,2

# Question

Ar_Q = np.ones([5,5])
Ar_Q[1:4,1:4] = np.zeros([3,3])
Ar_Q[2,2] = 9
print(Ar_Q)

# using the copy function and issue with assignment 

a = np.array([1,2,3])

b = a.copy()
d = a.copy()

print(b)

c = d

d[1] = 100

print(c)

# c and d point to same memory location when using assignment so changes appear on both.

## Mathematics, Statistics methods.

## Reorganizing methods

    # reshape method, vstack, h stack

## Loading files

    # genfromtext method.
    # convert float to int type using astype method.
    
## Boolean masking and Advanced indexing

    # we can index using a list. We can give a list of all position we need to get that data.
    
    # np.any and np.all method

