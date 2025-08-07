def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_rotations(s):
    return [int(s[i:] + s[:i]) for i in range(len(s))]

circular_primes = []

for num in range(2, 1000000):
    s = str(num)
    if any(d in s for d in "024568"):
        if num not in (2, 5):
            continue
    rotations = get_rotations(s)
    if all(is_prime(r) for r in rotations):
        circular_primes.append(num)

print(len(circular_primes))