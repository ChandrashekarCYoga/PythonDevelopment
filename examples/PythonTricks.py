# Ordered Sets

countries = ['China',
             'USA',
             'UK',
             'China', ]

print(set(countries))


# To preserve the order, you can do:

print(sorted(set(countries), key=countries.index))


# Set Comprehension
print({x+1 for x in range(5)})

# Switching Variables
a, b = [1, 2]

a, b = b, a

print({x: x+1 for x in range(5)})

print(a, b)
