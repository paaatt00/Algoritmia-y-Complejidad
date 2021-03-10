def isPerfect(num):
    n = 0
    for i in range(1, num):
        if num % i == 0:
            n = n + i
    return n == num

print(isPerfect(6))