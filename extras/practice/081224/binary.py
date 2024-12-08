def is_binary(num):
    while num > 0:
        digit = num % 10
        if digit not in [0,1]:
            return False
        num = num // 10
    return True

num = int(input("Please enter a number: "))
if is_binary(num):
    print("Binary.")
else:
    print("Not binary")
