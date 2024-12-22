# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.

num = int(input("Enter a number: "))
sum = 0
for i in range(1, (num//2)+1):
    remainder = num % i
    if remainder == 0:
        sum = sum + i
if sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")