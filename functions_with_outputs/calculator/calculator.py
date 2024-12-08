def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
}

# for ops in operations:
#     if ops == "*":
#         print(mul(4,8))

# print(operations['*'](4,8))

print("Welcome to your calculator...")
input1 = (float(input("Input 1: ")))

operator = input("What would you like to do? Type any (+ - * /): ")
input2 = (float(input("Input 2: ")))

calculation = operations[operator](input1, input2)

print(f"Result: {calculation}")

ifcontinue = input("Do you want to continue with the previous calculation? Type (y or n): ")

while ifcontinue == 'y':
    operator = input("What would you like to do? Type any (+ - * /): ")
    input2 = (float(input("Input 2: ")))

    calculation = operations[operator](calculation, input2)

    print(f"Result: {calculation}")
    ifcontinue = input("Do you want to continue with the previous calculation? Type (y or n): ")
