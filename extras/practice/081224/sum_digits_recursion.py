def sum_of_digits(num):
    if num < 10:
        return num
    else: 
        return (num % 10 + sum_of_digits(num // 10))

number = int(input("Enter a number: "))
print("Sum of digits: ", sum_of_digits(number))
