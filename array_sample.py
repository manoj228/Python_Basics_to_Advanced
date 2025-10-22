'''
import array  # module helps to declare array
from array import *  # other way of declaring it

array(type_of_array, [elements of array])

typecode -> gives the data type of 

arr.index(element) # provides element index by searching in array
'''

from array import *

vals = array('i', [10, 20, 30, 40])

print('arr values ', vals)

# copying vals to new Arr in one line
newArr = array(vals.typecode, (element * element for element in vals))

print('new Arr Values ', newArr)

print('Index of 40 ', vals.index(40))