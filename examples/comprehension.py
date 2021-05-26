#list, set, dictionary


my_list = []
for char in 'Hello':
    my_list.append(char)

print(my_list)


my_list1 = [char for char in 'hello']

print(my_list1)


my_list2 = [num for num in range(0, 100)]
print(my_list2)

my_list3 = [num*2 for num in range(0, 100)]
print(my_list3)

my_list4 = [num**2 for num in range(0, 100)
            if num % 2 == 0]

print(my_list4)


# Set
# No duplicates

my_set = {char for char in 'Hello'}
print(my_set)

my_set2 = [num for num in range(0, 100)]
print(my_set2)

# Dict
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)

my_dict = {key: value**2 for key, value in simple_dict.items()
           if value % 2 == 0}
print(my_dict)

my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)
