def isPrime(num):
    b = True
    for i in range(2, num):
        if num % i == 0:
            b = False
    return b

print(isPrime(12))
