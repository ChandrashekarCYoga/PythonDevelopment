# Dictionary

dictionary = {'a': [1, 2, 3], 'b': 'hello', 'x': True}

my_list = [{
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}, {
    'a': [4, 5, 6],
    'b': 'hello',
    'x': True
}]
print(dictionary['b'])

# gives error
#print(dictionary['c'])

print(dictionary)

print(my_list[0]['a'][2])

dictionary = {123: [1, 2, 3], True: 'hello'}

# key should be immutable
print(dictionary[123])
print(dictionary[True])

#this gives error
#print(dictionary[100])

#key has to be unique

#Dict Methods

user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}

user2 = dict(name='JohnJohn')

print(user.get('age', 55))

print(user2)

print('age' in user.keys())
print('hello' in user.values())

print(user.items())

# copy dict to another dict
user3 = user.copy()
user.clear()
print(user)
print(user3)

# removes actual value
print(user3.pop('age'))
print(user3)

# randomly removes some pair of key-value
print(user3.popitem())
print(user3)

print(user3.update({'age': 55}))
print(user3)
