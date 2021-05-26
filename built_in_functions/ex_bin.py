def int2bin(integer):
    """Function that converts an integer to a binary string"""
    try:
        binary = bin(integer)
        return binary[2:]  # string slicing to elimininate the prefix '0b'

    except TypeError:
        print('An integer should be provided as input')


print(int2bin(5))
# '101'

print(int2bin(6))
# '110'

print(int2bin(4.0))
# An integer should be provided as input
