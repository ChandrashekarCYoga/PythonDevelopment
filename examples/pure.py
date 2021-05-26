# Pure Functions
# Doesn't effect outside world
# keep data and implementation separate
from functools import reduce

wizard = {
    'name': 'Merlin',
    'power': 50
}


def attach(character):
    pass


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))

my_list = [1, 2, 3]


def multiply_by2_map(item):
    return item*2

# map, filter, zip and reduce


print(list(map(multiply_by2_map, my_list)))
print(my_list)


def only_odd(item):
    return item % 2 != 0

# filter


print(list(filter(only_odd, my_list)))
print(my_list)


# zip

your_list = [10, 20, 30]
their_list = [5, 4, 3]

print(list(zip(my_list, your_list, their_list)))
print(my_list)


# reduce

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))

print(my_list)
