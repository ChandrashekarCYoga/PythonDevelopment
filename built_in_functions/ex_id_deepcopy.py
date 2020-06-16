# list of numbers
numbers = [1, 2, 3, 4, 5]

# new list of numbers
new_numbers = numbers

# both list have the same id number
print(f'numbers id: {id(numbers)}, new_numbers id: {id(new_numbers)}')
# numbers id: 1836112528136, new_numbers id: 1836112528136

# we can also check that they refer to the same object with the identity operator is
print(numbers is new_numbers)
# True


import copy

# list of numbers
numbers = [1, 2, 3, 4, 5]

# new list of numbers
new_numbers = copy.deepcopy(numbers)

# both list have different id numbers
print(f'numbers id: {id(numbers)}, new_numbers id: {id(new_numbers)}')
# numbers id: 1836112528648, new_numbers id: 1836112763528

# we can also check that both variables point to different objects with the identity operator is
print(numbers is new_numbers)
# False