"""
How to merge two dictionaries
in paythong 3+
"""


x = {'a':1, 'b':2}
y = {'b':3, 'c':4}


z = {**x, **y}

print(z)
