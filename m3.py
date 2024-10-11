def multiplier(a):
    def multiply(b):
        return a*b
    return multiply
multiply_second_number=multiplier(5)
result = multiply_second_number(10)
    
print("multiplication of the number ",result)
 