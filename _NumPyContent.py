# NumPy - linear algebra, almost all other data science packages, rely on numpy
# array (1d vectors and matrices)

import numpy as np
import streamlit as st

st.write("* Cast list into a array")
my_list = [1,2,3]
arr = np.array(my_list)
st.write(
    arr,
    arr.shape,
    arr.dtype,
    type(arr)
)

st.write("* Cast a list of list to make a matrix (2d array)")
my_matrix = [[1,2,3],[4,5,6],[7,8,9],[15,15,10]]
arr = np.array(my_matrix)
st.write(
    arr,
    arr.shape,
    arr.dtype,
    type(arr)
)


st.write("* Return spaced values within a given interval")
arr = np.arange(start=1,stop=8,step=1)
st.write(arr, arr.shape,type(arr))


# Generate arrays of zeros or ones
arr = np.zeros((5,4))
print(arr, end='\n\n')

arr = np.ones((3,3))
print(arr, end='\n\n')

# np.linspace(start,stop,n_points)
# np.eye(diagonal)


# Numpy also has lots of ways to create random number arrays:

np.random.seed(seed=1)
# random samples from a uniform distribution over [0, 1)
arr = np.random.rand(2,2) 
print(arr, end='\n\n')


# random integers from low (inclusive) to high (exclusive).
arr = np.random.randint(low=1, high=100, size=30)
print(arr, end='\n\n')


# reshape() method
arr = arr.reshape(5,6)
print(arr, end='\n\n')


print(
    arr.argmax()
)
# .max()  .min()   
# argmax() , argmin() index location of max



# slice notation to pickup elements  [8]  [1:5] [:7] [4:]
print(
    arr[2:,3:]
)



# broadcast - copy and reference of array  .copy()
# arr_2d[1,1]
# arr_2d[:2,1:]
# conditional selection  arr>5 (bool arr, used as index selection)  arr[arr>5]
# math operations with array (+ - * /  **2  )  np.sqrt , np.exp(), np.sin(), np.log()   ufunc on numpy doc

# exercise
# create array, 1d, 2d, 
# index selection
# get sum of all, summ of all cols

# np.arange(10,51,2)
# np.arange(0,8).reshape(3,3)  - create 3x3 matrix with values ranging from 0 to 8
# np.random.randn(25)  25 random numbers sampled from a  std normal distribution

# mat = np.arange(1,26).reshape(5,5)     show a slice of matrix and ask student to slice mat[2:,1:]
# mat.sum()   np.sum(mat)
# mat.sum(axis=0)