first, second = 0, 1

n = int(input("Please enter a number to generate the Fibonacci series: "))

print("The Fibonacci series is: ")
for i in range(0, n):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result)
