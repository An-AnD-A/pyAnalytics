# NumPy Tutorial

import numpy as np

# Making an array using list
lst1 = [1.0,2.5,3.6]
lst2 = [3.5,6.5,7.8]
Ar1 = np.array([lst1,lst2])
print(Ar1)


# Arrays of different dimensions
x0 = np.random.randint(10)                     # Scalar    
x1 = np.random.randint(10, size = (2))         # 1D array
x2 = np.random.randint(10, size = (2,3))       # 2D array
x3 = np.random.randint(10, size = (2,3,5))     # 3D array
print(x0)
print(x1)
print(x2)
print(x3)

# NOTE : The object type is numpy.ndarray for all except for Scalar (i.e. x0)

x5 = np.random.rand(10)  #rand gives value between 0 and 1 so argument is the shape of array.
print(x5)
x6 = np.random.randint(5,10, size = (3,3),dtype = "int16") # Integer between 5 and 10(high value exclusive) 
print(x6)
x7 = np.random.random((3,5)) # Gives a float between 0.0 and 1.0
print(x7)                    # .random() and .random_sample() are same methods
x8 = np.random.randn(3)      # returns samples from a standard normal distribution.
print(x8)


# Dimensions and Size.
Ar1.ndim                # Gives the dimension of the array.
Ar1.shape               # Gives a tuple 
print(type(Ar1.shape))  
Ar1.dtype               # The data type of elements in the array.
Ar1.itemsize            # Bytes used by one array element.
Ar2 = np.array([1 , 2, 3], dtype = 'int16') # Specify the Byte size to make code efficient.Default is int32
Ar2.dtype 
Ar2.itemsize          
Ar2.size                # Gives the total number of elements
Ar2.nbytes              # Total bytes used by array
total_size = Ar2.size*Ar2.itemsize # Calculating manually the Bytes used by array.
print(total_size)


# Getting Specific elements

Ar = np.array([[2,3,6,3,8,5,9,4],[4,7,2,5,9,2,6,1]], dtype = 'int32')
Ar[1,4]    # Getting one element based on index
Ar[0,:]    # First Row
Ar[:,4]    # 5th Column
Ar[:,2:6]  # Column 3 to 6. high value not inclusive
# Using stepsize.
Ar[0,1:6:2]   # Ar[row index, column start:Column_end:step]
Ar[:,::2]     # Getting alternate columns
Ar[::2,:]     # Getting alternate rows.


# Changing Elements

Ar[0,4] = 20    # Changing one element in array
print(Ar)
Ar[0,0:4] = 5   # Changes all the given index location value to 5.
print(Ar)
Ar[0,0:4] = [ 3,4,5,6]
print(Ar)
# 3D arrays and index location
Ar_3d = np.array([[[1,2],[2,1]], [[2,1],[1,2]]])
print(Ar_3d)
Ar_3d [1,0,1]
Ar_3d[1,:,:] = [[3,3],[3,3]]
print(Ar_3d)


## Initializing Special Arrays using Functions

Ar_3 = np.ones([4,3])                   # All 1's
print(Ar_3)          
Ar_4 = np.zeros([4,3])                  # All 0's
print(Ar_4)
Ar_5 = np.identity(4)                   # Identity matrix
print(Ar_5)
print(np.full([3,3],5,dtype ="int16"))  # All elements are 5. np.full(size,fill value)
print(np.full_like(Ar_3d,5))            # Size specified by an existing array
print(np.full(Ar_3d.shape,5))           # Gives same output as full_like.
Ar_6 = np.eye(3,5,k =-1,dtype="int16")  # np.eye(row,column,k value,dtype). K value refers to the diagonal.
print(Ar_6)                    # k>1 means upper diagonal,k<1 means lower diagonal, k=0 principal diagonal 

# Question : make the matrix 
#    [1,1,1,1,1
#     1,0,0,0,1
#     1,0,9,0,1
#     1,0,0,0,1
#     1,1,1,1,1]

Ar_Q = np.ones([5,5])
Ar_Q[1:4,1:4] = np.zeros([3,3])
Ar_Q[2,2] = 9
print(Ar_Q)

Ar_7 = np.linspace(50,100,num=11,endpoint=True,axis=0) #(start,end,number of samples,endpoint included(T/F,axis))
Ar_7

# Manipulating Matrix

Ar_7 = np.repeat([[[1,2],[3,4]],[[5,6],[7,8]]],[2,2],axis = 2) #np.repeat(matrix,axis of repetition)
print(Ar_7)
# axis order is z,y,x = 0,1,2. Default is along x axis

Ar_8 = np.tile([1,2,3,4],(2,3,4)) #np.tile(repeated matrix,reps along the axis)
print(Ar_8)

Ar_9 = np.empty_like(Ar_8) # Gives an empty matrix
print(Ar_9)
Ar_10 = np.reshape([0,1,2,3,4,5,6,7,8,9],(1,-1))# np.reshape(matrix,new shape)
print(Ar_10) # -1 will adjust the shape to be compactible with the given row or column value for new matrix


# using the copy function and issue with assignment 
a = np.array([1,2,3])
b = a.copy()
d = a.copy()
print(b)
c = d
d[1] = 100
print(c)
# NOTE :c and d point to same memory location when using assignment so changes appear on both.

print(np.arange(5,20,2))  # creates an Array for the start,end and step given.

Ar_11 = np.array([2,4,6,8]).reshape((2,-1))
Ar_12 = np.array([1,3,5,7]).reshape((2,-1))
Ar_11
Ar_12
np.hstack((Ar_11,Ar_12))  # pass the array as tuple.
np.vstack((Ar_11,Ar_12))  # pass the array as tuple.
np.concatenate((Ar_11,Ar_12),axis=0)

    #np.delete,
    #np.append,
    
## Matrix operations 

x9 = np.array([2,4,6,5,9,4,6,2]).reshape((4,-1))
x10 = np.array([4,6,2,9,4,3,7,4]).reshape((-1,4))    
mat_mul_x9_x10 = x9.dot(x10)    # Dataframe.dot() gives the matrix multiplication
mat_mul_x9_x10


    # how to find the inverse.
    # np.cumsum()
  
## Mathematics, Statistics methods.
    
    # create normally distribured values. np.random.normal(mu,sigma,10000)
    
## Loading files

    # genfromtext method.
    # convert float to int type using astype method.
    
## Boolean masking and Advanced indexing

    # we can index using a list. We can give a list of all position we need to get that data.
    
    # np.any and np.all method

