import array

# This array will store integer type elements
arr_int = array.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", arr_int.tolist())

# This array will store Unicode characters (Python 3.x)
# In Python 3, 'u' for Unicode is not supported in array module, so we use a list of characters.
# If you need to work with characters, you might use a list instead.
# For example:
arr_char = list('abc')  # List of characters
print("Character Array:", arr_char)

# This array will store float type elements
arr_float = array.array('f', [1.0, 2.0, 3.0])
print("Float Array:", arr_float.tolist())