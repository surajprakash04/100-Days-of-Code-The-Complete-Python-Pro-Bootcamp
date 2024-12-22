def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_between(lower, upper):
    primes = []
    for num in range(lower, upper + 1):
        if is_prime(num):
            primes.append(num)
    return primes

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

result = prime_between(lower, upper)
if result == []:
    print("No Prime Number in the given range.")
else:
    print(f"Prime number in the given range: {result}")
