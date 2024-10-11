def print_formatted(number):
    # Find the width of the largest binary number
    width = len(bin(number)) - 2

    # Loop through 1 to the number
    for i in range(1, number + 1):
        # Print the number in decimal, octal, hexadecimal, and binary format
        # All values are padded with spaces to align correctly
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")
