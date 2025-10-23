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