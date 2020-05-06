# set

# unique items

my_set = {1,2,3,4,5,5}

print(my_set)

my_set.add(100)

print(my_set)

# can't add, its not unique
my_set.add(2)
print(my_set)

my_list = [1,2,3,4,5,5]

print(set(my_list))

# doesn't support indexing

#print(my_set[0])

print(len(my_set))

print(list(my_set))

new_set = my_set.copy()

my_set.clear()

print(new_set)
print(my_set)

my_set = new_set.copy()
# Methods

your_set = {4,5,6,7,8,9,10}

print(my_set.difference(your_set))
my_set.discard(5)
print(my_set)

my_set.add(5)
print(my_set)

print(my_set.difference_update(your_set))
print(my_set)

my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}

print(my_set.intersection(your_set))

print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))

print(my_set | your_set)
print(my_set & your_set)


my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.issubset(your_set))

print(your_set.issuperset(my_set))