n = int(input("Please enter a number: "))
print("Before reversal: ", n)
reverse = 0
while n != 0:
    reverse = reverse * 10 + n % 10
    n = n // 10
print("Reversed: ", reverse)
