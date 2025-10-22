'''
to get user input

x = int(input('Enter a number'))

-------------

# eval input 2 + 3 - 1 
it is not a int / float / string
use eval to evaluate string

----------------

to get command line arguments as input

import sys

when u run "python input.py 4 5"
                    argv[0] [1] [2] 
    

'''

x = int(input('Enter a number '))
print(x)

print(eval('2 + 5 - 1'))

import sys
x = int(sys.argv[1])
print(x)