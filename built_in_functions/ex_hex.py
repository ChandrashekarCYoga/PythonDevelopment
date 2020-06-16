'''
The hex(x) function converts an integer number to a lowercase hexadecimal string. 
This string starts with the prefix ‘0x’, indicating is a hexadecimal number. 
The function raises an exception (TypeError) if an object different than an integer 
is provided as input
'''

# convert the integer 10 into a hexadecimal number
hex_number = hex(10)

print(hex_number)
# 0xa
print(type(hex_number))
# <class 'str'>

# An exception is raised if a float is provided as input
# hex_number = hex(10.0)
# TypeError


def rgb_to_hex(rgb_triple):
    """

    Function that maps a RGB tuple representation to a hexadecimal string

    Parameters:
    rgb_triple (tuple): RGB tuple representation (red, green, and blue)

    Returns:
    hex_string (string): Hexadecimal string representation '0xRRGGBB'

    """
    hex_string = ''
    # we loop through the red, green, blue values of the tuple rgb_tuple
    for integer in rgb_triple:
        # string slicing to elimininate the prefix '0x'
        hexadecimal = hex(integer)[2:]
        if len(hexadecimal) == 1:
            hexadecimal = '0' + hexadecimal  # pad the string to the left with a 0
        hex_string += hexadecimal
    return '#' + hex_string


# call the function
color_1 = (255, 255, 255)
color_2 = (255, 255, 0)
color_3 = (70, 90, 200)

color_1_hex = rgb_to_hex(color_1)
# '#ffffff'
print(color_1_hex)
color_2_hex = rgb_to_hex(color_2)
# '#ffff00'
print(color_2_hex)
color_3_hex = rgb_to_hex(color_3)
# '#465ac8'
print(color_3_hex)