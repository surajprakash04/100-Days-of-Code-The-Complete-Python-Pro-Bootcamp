# SQUARE
# num = int(input("Provide a number: "))
# print(f"Square = {num*num}")

# CUBE
# num = int(input("Provide a number: "))
# print(f"Cube = {num*num*num}")

# SQUARE ROOT
import math

num = int(input("Enter a number: "))
if num < 0:
    print("Negative numbers can't have square roots.")
else:
    print(f"Square roots = {math.sqrt(num)}")
    