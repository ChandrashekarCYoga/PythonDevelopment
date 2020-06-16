'''
The zip function can accept any type of iterable such as lists, strings, tuples, 
or dictionaries, returning an iterator object. To visualize this object, 
we can convert it into a list with the built-in function list().
'''

# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

# iterator of tuples - containing each tuple a product and its price
print(zip(products, prices))
# <zip at 0x1ab80c8b788>

# to visualize the iterator we have to convert it into a list
print(list(zip(products, prices)))
# [('table', 50), ('chair', 20), ('sofa', 200), ('bed', 150), ('lamp', 10)]



# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']

# list of prices
prices = [50, 20, 200, 150, 10]

for product, price in zip(products, prices):
    print(f'Product: {product}, Price: {price}')
