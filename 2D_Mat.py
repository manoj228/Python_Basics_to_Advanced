'''
numpy is used for multi-dimensional array, we have to install it manually

array()
   -> arr = array([1, 2, 3])
   -> arr.dtyp # print type of arr elements
   -> if we change int to float in arr, all array elements will be implicitly converted into float  eg: arr = array([1, 2, 3.0])

linspace(start, end, split)
  -> divides the range from start to end by split # split default is 50

logspace(start, end, split)
  -> split the array by logbase10staart 

arange(start, end, increment)
  -> it will begin from start to end and increase the increment iteration


zeros(size) 
  -> fill the arr with zeros

ones(size)
  -> fill the arr with ones 

'''

from numpy import *

arr = array([1, 2, 3, 4, 5])
print('Arr:', arr)

arr = linspace(0, 15)
print('Linspace arr:', arr)

arr = arange(1, 15, 2)
print('Arange arr:', arr)

arr = logspace(1, 40, 5)
print('Logspace arr:', arr)

arr = zeros(5, int)
print('Zeros arr:', arr)    

arr = ones(5, int)
print('ones Arr:', arr)

# ----------------------------------------------------------------------

arr1 = array([1, 2, 3])

arr2 = arr1.view() # copying array with same memory       (shallow copy)
arr3 = arr1.copy() # copying array with different memory  (deep copy)

arr1[0] = 10

print('Arr2', arr2)
print('Arr3', arr3)

# ----------------------------------------------------------------------

# matrix multiplication

arr1 = array([ [1, 2, 3, 10, 20, 30], 
               [4, 5, 6, 40, 50, 60]])

print('Element size', arr1.size)   # print overall element size 
print('Row and Col', arr1.shape)    # print row and column

arr2 = arr1.flatten()   # 2D arr into 1D arr
print('2D to 1D arr2', arr2)

arr3 = arr2.reshape(3, 4)      # 1D arr into 2D arr
print('\n1D to 2D arr\n', arr3)

arr4 = arr2.reshape(2, 2, 3)  # 1D arr into 3D arr
print('\n1D into 3D arr\n', arr4)

m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')        # matrix
m2 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')  

m3 = m1 * m2
print('Matrix multiplication: ', m3)