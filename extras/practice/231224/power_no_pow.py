base = int(input("Enter the value for base: "))
exponent = int(input("Enter the value for exponent: "))
result = 1

print(f"{base} to power {exponent} =", end=" ")
while exponent != 0:
    result = result * base
    exponent = exponent - 1
print(result)
