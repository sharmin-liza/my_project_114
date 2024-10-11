def print_formatted(number):
    # Find the width of the binary representation of the largest number
    width = len(bin(number)[2:])
    
    # Loop through all numbers from 1 to number
    for i in range(1, number+1):
        # Print decimal, octal, hexadecimal (capitalized), and binary representations
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    try:
        n = int(input())  # Try to get input
        print_formatted(n)
    except EOFError:
        print("Input was not provided or an unexpected end of input occurred.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
