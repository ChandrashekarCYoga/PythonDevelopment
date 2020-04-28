#operator precedence

# ()
# **
# * /
# + -


print((20 - 3) + 2 ** 2)

# 45.0
print((5 + 4) * 10 / 2)

# 45.0
print(((5 + 4) * 10) / 2)

# 45.0
print((5 + 4) * (10 / 2))

# 25
print(5 + 4 * 10 // 2)


print(bin(128))

print(bin(5))

print(int('0b101', 2))