def prime_check(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False       
    return True

sum = 0

for i in range(2, 2000000):
    if prime_check(i):
        sum += i

print(sum)