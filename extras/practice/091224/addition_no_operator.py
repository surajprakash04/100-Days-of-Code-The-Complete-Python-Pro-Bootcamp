def main():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    
    while y != 0:
        temp = x & y
        x = x ^ y
        y = temp << 1
    
    print("Sum =", x)

main()