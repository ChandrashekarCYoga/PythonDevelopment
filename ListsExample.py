l1 = [1,2,3,4,5]
l2 = ['a','b','c','d']
l3 = [1, 2, 'a', True]

print(l1)
print(l2)
print(l3)


amazon_cart = [
  'notebooks', 
  'sunglasses',
  'toys',
  'grapes']

print(amazon_cart[0])
print(amazon_cart[1])

print(amazon_cart[-1])
print(amazon_cart[-2])

# List slicing

print(amazon_cart[:])

print(amazon_cart)
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
print(amazon_cart)
print(amazon_cart[0:3])

basket = [1,2,3,4,5]
print(len(basket))

basket.append(6)

print(basket)

new_list = basket.append(100)
print(new_list)
new_list = basket
print(new_list)

basket.insert(4, 400)
print(basket)


basket.extend([100,101])
print(basket)

#removing
basket.pop()
print(basket)

basket.pop(0)
print(basket)

basket.remove(400)
print(basket)

new_list = basket.remove(100)
print(new_list)

new_list = basket.pop()
print(new_list)

basket.clear()
print(basket)

basket = ['x','a','b','c','d','e','d']

print('d' in basket)
print('x' in basket)

print('i' in 'i am chandra')

print(basket.count('d'))

print(sorted(basket))

print(basket)

basket.reverse()
print(basket)

new_list = basket.copy()
print(new_list)

