def fun():
    print('Hello')


def call(a, *b): # denotes multiple arguments
    print(a)
    print("tuple", b)

def person(name, **data): # denotes multiples arguments with key
    print(name)
    
    for i, j in data.items():
        print(i, j)


fun()   # normal function call
call(5, 1, 2, 3, 4,)  # passing multiple arguments 
person('manoj', age=27,city='Bengaluru')  # passing arguments with keys