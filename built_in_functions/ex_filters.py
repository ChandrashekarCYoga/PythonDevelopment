'''
The filter function accepts as second argument any type of iterable such as lists, 
strings, tuples, or dictionaries, returning an iterator object. To visualize this object, 
we can convert it into a list with the built-in function list().
'''

# list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# get odd numbers
print(list(filter(lambda x: x % 2, numbers)))
# [1, 3, 5]


# get even numbers
print(list(filter(lambda x: x % 2 == 0, numbers)))
# [2, 4, 6]



# list of cities
cities = ('Madrid', 'Valencia', 'Barcelona', 'Munich', 'Stuttgart')

# cities that start with M or VMSError(" error")
print(tuple(filter(lambda x: x.startswith(('M', 'V')), cities)))
# ('Madrid', 'Valencia', 'Munich')