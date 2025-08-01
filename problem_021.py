def sum_of_divisors(x):
    total = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            total +=i
            if i != x // i:
                total += x // i
    return total

amicable_numbers = set()

for a in range(2, 10000):
    b = sum_of_divisors(a)
    if b != a and sum_of_divisors(b) == a:
        amicable_numbers.add(a)
        amicable_numbers.add(b)

print(sum(amicable_numbers))