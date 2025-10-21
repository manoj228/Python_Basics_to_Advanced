'''
list -> mutable and  it can have any number of data

for eg: nums = ['manoj', 4, 2.9]  // valid 

to insert:
nums.insert(index, element)
nums.pop(index)             // remove element at index
nums.pop()                  // remove last element and print it [similar to stack]
nums.remove(element)
del nums[start_pos : end_pos]  // remove all elements from start till end
nums.extend([12, 3, 2, 10]) // add as many elements 
max(nums)
min(nums)
sum(nums)
len(nums)
nums.sort()   // sort all elements

'''
 
nums = ['manoj', 4, 2.9]
print(nums)

nums.insert(0, 10)
print(nums)

nums.pop(2)             # remove element at index
print(nums)

print(nums.pop())                  # remove last element and print it [similar to stack]

nums.remove(10)
print(nums)


del nums[0 : 1]  # remove all elements from start till end
print(nums)

nums.extend([12, 3, 2, 10]) # add as many elements 
print(nums)

print(max(nums))
print(min(nums))
print(sum(nums))
print(len(nums))

nums.sort()   # sort all elements
print(nums)