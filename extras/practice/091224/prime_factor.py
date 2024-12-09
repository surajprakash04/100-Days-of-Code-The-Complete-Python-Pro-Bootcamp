def prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

num = int(input("Enter a number: "))
result = prime_factors(num)
print("Prime Factors of", num, ":", result)
