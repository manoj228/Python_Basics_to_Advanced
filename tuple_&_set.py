'''
tuple -> immutable 

tup = (10, 20, 30)        # storing element
tup.count(10)             # frequencies of an element

'''

print('tuple\n')
tup = (10, 20, 30)        # storing element

print(tup)

print('frequency of 10 is ', tup.count(10))             # frequencies of an element

'''
# removes the duplicates and it is unordered by default
set = {22, 24, 28, 26} 

# we can't access through index
set.add(10)  # add element

'''
print('\n------------------------------------\n')
print('Set')
# removes the duplicates and it is unordered by default
set = {22, 24, 28, 26, 28} 

print(set)

# we can't access through index
set.add(10)  # add element
print(set)