n = int(input("Please enter a number: "))
temp = n

#reverse the number
reverse = 0
while temp != 0:
    reverse = reverse * 10 + temp % 10
    temp = temp // 10
# check if the number is a palindrome
if reverse == n:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
