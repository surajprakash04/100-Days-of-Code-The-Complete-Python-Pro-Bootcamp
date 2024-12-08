def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num % 10) + str(reverse(num // 10)))

def is_palindrome(num):
    if num == reverse(num):
        return True
    else:
        return False

n = int(input("Please enter a number: "))
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not a Palindrome")
