import numpy as np

# one-dimensional array
array_1d = np.array([1.1, 9.2, 8.1, 4.7])
#print(array_1d.shape)
#print(array_1d[2])

array_1d.ndim #returns the dimension (in this case: 1)



# two-dimensional array
# This array has 2 rows and 4 columns. 
# NumPy refers to the dimensions as axes, 
# so the first axis has length 2 and the second axis has length 4.
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

# Heres how to access the 3rd value in the 2nd row:
array_2d[1,2]


# To access an entire row and all the values therein, 
# you can use the : operator

# Heres the entire first row: 
array_2d[0, :]



# An array of 3 dimensions (or higher) is often referred to as a tensor. 

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

#printing 18
mystery_array[2,1,3]

#getting a (3,2) matrix with the values [[ 0, 4], [ 7, 5], [ 5, 97]]
first_values_array = np.array([
    [mystery_array[0,0,0],mystery_array[0,1,0]],
    [mystery_array[1,0,0],mystery_array[1,1,0]],
    [mystery_array[2,0,0],mystery_array[2,1,0]],
])
#or
first_values_array = mystery_array[:, :, 0]


# if
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
# then, v1+v2 = [ 6, 6, 5, 10]
# Multiplying the two vectors together also results in an element by element operation

# in contrast, if
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
# then, list1+list2 = [4, 5, 2, 7, 2, 1, 3, 3]






# Use .arange()to createa a vector a with values ranging from 10 to 29. 
a = np.arange(start=10,stop=30) #last num excluded

# Create an array containing only the last 3 values of a
a[-3:]
# Create a subset with only the 4th, 5th, and 6th values
a[3:6]
# Create a subset of a containing all the values except for the first 12 (i.e., [22, 23, 24, 25, 26, 27, 28, 29])
a[12::]
# Create a subset that only contains the even numbers (i.e, every second number)
a[::2]
# Reverse the order of the values in a, so that the first element comes last
a[::-1]



# Print out all the indices of the non-zero elements in this array: 
array1 = [6,0,9,0,0,5,0]
non_zero = np.nonzero(array1)


# generate a 3x3x3 array with random numbers
from numpy.random import random
random_array = random((3,3,3))


# Use .linspace() to create a vector x of size 9 with values spaced out evenly between 0 to 100 (both included).
vector1 = np.linspace(start=0,stop=100,num=9)

# Use NumPy to generate an array called noise with shape 128x128x3 that has random values. 
# Then use Matplotlib's .imshow() to display the array as an image.
noise = np.random.random((128,128,3))
# plt.imshow(noise)





# We can reverse the order of rows and columns with .flip() and .rot90 (or some other angle) to rotate them


