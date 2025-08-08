def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    s = str(n)
    
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False

    for i in range(len(s) - 1, 0, -1):
        if not is_prime(int(s[:i])):
            return False

    return True

truncatable_primes = []
n = 11

while len(truncatable_primes) < 11:
    if is_prime(n) and is_truncatable(n):
        truncatable_primes.append(n)
    n += 2

print(sum(truncatable_primes))
