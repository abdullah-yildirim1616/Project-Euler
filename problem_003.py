import math
def prime_check(x):
    is_prime = True

    for i in range(2, int(math.sqrt(x)) +1):
        if x % i == 0:
            is_prime = False
            break
    return is_prime
number = 600851475143

biggest_prime = 1

for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0 and prime_check(i):
        biggst_prime = i

print(biggst_prime)