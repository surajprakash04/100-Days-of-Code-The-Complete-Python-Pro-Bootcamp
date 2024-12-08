n1 = int(input("First number (n1): "))
n2 = int(input("Second number (n2): "))
n3 = int(input("Third number (n3): "))

if n1 >= n2 and n1 >= n3:
    print("greatest: n1")
elif n2 >= n1 and n2 >= n3:
    print("greatest: n2")
else:
    print("greatest: n3")
    