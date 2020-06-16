'''
The map function can be very useful when we want to apply 
a mathematical operation to all the elements of an iterable.
'''

# list of numbers
numbers = [1, 2, 3, 4, 5]

print(numbers)

# add 1
print(list(map(lambda x: x + 1, numbers)))
# [2, 3, 4, 5, 6]

# multiply by 2
print(list(map(lambda x: x * 2, numbers)))
# [2, 4, 6, 8, 10]

# obtain the cube
print(list(map(lambda x: x ** 3, numbers)))
# [1, 8, 27, 64, 125]



# add 1 funtion - regular function
def add_one(element):
    return element + 1 

# add 1 to each element of the list
print(list(map(add_one, numbers)))
# [2, 3, 4, 5, 6]



# lists of numbers
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

# multiply the elements of both lists
print(list(map(lambda x, y: x * y, numbers_1, numbers_2)))
# [6, 14, 24, 36, 50]
