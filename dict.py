'''
dict -> key - value pairs (similar to map in c++)
dict = {1 : 'manoj', 2 : 'kumar'}       # key should be unique and immutable
print(dict)

dict[hash_key]        # access through key

print(dict.get(index))  # access through index

print(dict.get(index, 'default value')) # if index is not found, print 'default value'

#we can have list and dictionary in dict
data = {'C++' : 'Vs', 'Python':['Pycharm', 'Sublime'], 'Java':{'JSE' : 'Netbeans'}}

'''

print('------------------------------------\n')
print('Dict')
data = {1 : 'manoj', 2 : 'kumar'}       # key should be unique and immutable
print(data)

print(data[2])   # access through key 

print(data.get(2))   # won't raise any error
# print(dict[3])       # will throw error    

print(data.get(3))  # print none
print(data.get(3, 'Not found'))


keys = ['manoj', 'kumar']
values = ['C++', 'Python']

# converting list into dict
dictionary = dict(zip(keys, values))
print(dictionary)

print(dictionary['manoj'])

# add new key-value pairs
dictionary['raj'] = 'Django'
print('After new value added', dictionary)

# to delete the data provide key
del dictionary['kumar']
print('After value deleted', dictionary)

data = {'C++' : 'Vs', 'Python':['Pycharm', 'Sublime'], 'Java':{'JSE' : 'Netbeans'}}
print('List & dict inside dictionary', data)


print('list for python key', data['Python'])

