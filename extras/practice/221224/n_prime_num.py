def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

def first_n_prime(n):
    prime_list = []
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            prime_list.append(num)
            count += 1
        num += 1
    return prime_list

n = int(input("Enter the range: "))
print(f"First {n} prime numbers are: {first_n_prime(n)}")
