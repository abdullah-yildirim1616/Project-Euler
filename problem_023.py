def sum_of_divisors(x):
    total_divisors = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            total_divisors += i
            if i != x // i:
                total_divisors += x // i
    return total_divisors

abundant_numbers = []
for i in range(1, 28124):
    if sum_of_divisors(i) > i:
        abundant_numbers.append(i)

abundant_sums = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        s = i + j
        if s <= 28123:
            abundant_sums.add(s)
        else:
            break
total = sum(i for i in range(1, 28124) if i not in abundant_sums)

print(total)