i = 0
result = 0

n = int(input("Please enter a number: "))
number1 = n
temp = n
while n != 0:
    n = n // 10
    i += 1
while number1 != 0:
    n = number1 % 10
    result += pow(n, i)
    number1 = number1 // 10
if temp == result:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
    