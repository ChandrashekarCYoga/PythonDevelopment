# store information in program

# snake_case
# start with lowercase or underscore
# _variables are private _variables
# variables are case sensitive
# don't overwrite keywords
# descriptive

user_iq = 190

user_age = user_iq / 4

print(user_iq)
print(user_age)

# constants
# value don't change
# don't create value with two underscore, not good practice

PI = 3.14

print(PI)

a, b, c = 1, 2, 3

print(a)

print(b)

print(c)

# augmented assignment operator
some_value = 5
some_value += 2
print(type(some_value))

print(some_value)

x = "Hello World"
print(x)
print(type(x))

long_string = '''
WOW
O O
---
'''
print(long_string)
print(type(long_string))

x = 20
print(x)
print(type(x))

x = 20.5
print(x)
print(type(x))

x = 1j
print(x)
print(type(x))

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

x = ("apple", "banana", "cherry")
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = {"name": "John", "age": 36}
print(x)
print(type(x))

x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

# Escape sequence
weather = "It\'s \"kind of\" sunny"
print(weather)

weather = "\tIt\'s \"kind of\" sunny"
print(weather)

name = 'Johnny'
age = 55

print(f'Hi {name}, You are {age} years old')

print('Hi {}. You are {} years old'.format('Johnny', '55'))

print('Hi {}. You are {} years old'.format(name, age))

print('Hi {0}. You are {1} years old'.format(name, age))

print('Hi {new_name}. You are {age} years old'.format(
    new_name='sally', age=100))

selfish = 'me me me'
#  01234567

print(selfish[0])

selfish = '01234567'
# [start:stop:stepover]
# string slicing
print(selfish[4:7:2])
print(selfish[1:])
print(selfish[:5])

print(selfish[::1])

print(selfish[-1])
print(selfish[-2])
print(selfish[-3])

# reverse
print(selfish[::-1])
print(selfish[::-2])

# strings are immutable in python

quote = 'to be or not to be'
print(quote.upper())
print(quote.upper().lower())

print(quote.capitalize())

print(quote.find('be'))

print(quote.replace('be', 'me'))

print(quote)
