# counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for item in my_list:
    counter += item

print(counter)

# special kind of object to iterate
print(range(10, 100, 2))

for number in range(10, 100, 10):
    print(number)

for _ in range(10, 0, -1):
    print(_)

for _ in range(2):
    print(list(range(10)))

#enumerate
# when you need index its useful
#upacking
for i, char in enumerate('helllloooo'):
    print(i, char)

for i, char in enumerate([1, 2, 3, 4, 5]):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is:{i}')
i = 0
while i < 10:
    print(i)
    if i == 5: break
    i += 1
else:
    print('done with all the work')

# when you are not sure when to exit, use while Loop
for item in my_list:
  # don't know what to implement yet
  pass

i = 0
while True:
    response = input('say something(say bye to exit):')
    if (response == 'bye'):
        break

for item in my_list:
    continue
    print(item)
