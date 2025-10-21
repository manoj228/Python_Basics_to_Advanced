'''
dict -> key - value pairs (similar to map in c++)
dict = {1 : 'manoj', 2 : 'kumar'}       # key should be unique and immutable
print(dict)

dict[hash_key]        # access through key

print(dict.get(index))  # access through index

print(dict.get(index, 'default value')) # if index is not found, print 'default value'

'''

print('------------------------------------\n')
print('Dict')
dict = {1 : 'manoj', 2 : 'kumar'}       # key should be unique and immutable
print(dict)

print(dict[2])   # access through key 

print(dict.get(2))   # won't raise any error
# print(dict[3])       # will throw error    

print(dict.get(3))  # print none
print(dict.get(3, 'Not found'))


keys = ['manoj', 'kumar']
values = ['C++', 'Python']
