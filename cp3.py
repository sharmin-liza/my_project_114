def print_rangoli(size):
    # Create a list to hold each line of the rangoli
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    lines = []
    
    # Create the rangoli lines for the top half including the middle line
    for i in range(size):
        # Slice the alphabet to get the desired portion and reverse it
        s = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        # Center the string with hyphens
        lines.append(s.center(4*size - 3, '-'))
    
    # Join the top half with the bottom half (which is a reversed version of the top half without the last line)
    print("\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    size = int(input())  # Read the input size
    print_rangoli(size)
