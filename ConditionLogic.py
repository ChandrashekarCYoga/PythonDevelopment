# booleans plays an important role

is_old = True
is_licensed = True

# if condition :
# evaluate

if is_old and is_licensed:
    print('you are old enough to drive!')

# completely new line
print("check check")

is_old = False

if is_old and is_licensed:
    print('you are old enough to drive!')
# elif is_licensed:
#     print('you can drive now')
else:
    print('you are not old enough to drive!')

#Truthy
print(bool('hello'))
print(bool(5))

#Falsey
print(bool(''))
print(bool(0))

password = '123'
username = 'johnnny'

if password and username:
    print('you are in :-)')

# Ternary Operator or conditional expressions

# condition_if_true if condition else condition_if_else

is_friend = True
can_message = 'message allowed' if is_friend else "not allowed to message"

print(can_message)

# Short Circuiting

is_User = True

print(is_friend and is_User)

if is_friend and is_User:
    print('best friends forever')

# Logical Operators

# And
# Or
# >
# <
# =

print(4 < 5)
print(4 > 5)
print(4 == 5)

print('hello' == 'hello')

print('a' > 'b')

print('a' > 'A')

print(0 >= 0)
print(0 != 0)

print(not (True))

print(not (1 == 1))

is_magician = True
is_expert = False

# check if magician AND expert : " you are a master magician"

# check if magician but not expert: "at least you're getting there"

# if you're not a magician: "you need magic powers"

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print("you're getting there")
elif not is_magician:
    print("you need magical powers")


print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
