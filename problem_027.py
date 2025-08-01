def prime_check(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False       
    return True

max_count = 0
product = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while prime_check(n**2 + a*n + b):
            n += 1
        if n > max_count:
            max_count = n
            product = a * b
    
print(product)