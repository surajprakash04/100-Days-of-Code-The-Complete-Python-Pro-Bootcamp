base = int(input("Enter the value for base: "))
exponent = int(input("Enter the value for exponent: "))
result = 1
print(f"The result of {base} raised to the power of {exponent} is", end=' ')
for exponent in range(exponent,0,-1):
    result *= base
print(result)
