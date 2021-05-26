# for loop

# strings
for item in 'Zero to Mastery':
    print(item)

# list
for item in [1, 2, 3, 4, 5]:
    print(item)

# tuple
for item in (1, 2, 3, 4, 5):
    print(item)

# sets
for item in {1, 2, 3, 4, 5}:
    print(item)
print(item)

# nested loop
for item in (1, 2):
    for x in ['a', 'b']:
        print(item, x)

# iterable - list, dictionary, tuple, set, string

# iterated -> one by one check ecah item in the collection

user = {'name': 'Golem', 'age': 5006, 'can_swim': False}

# itrerating through dictionary
for key, value in user.items():
    print(key, value)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# Not iterable, only collections and objects
# for item in 50:
#   print(item)
