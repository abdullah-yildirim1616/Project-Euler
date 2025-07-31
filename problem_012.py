def count_divisors(x):
    count = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            count += 2 if i != x // i else 1
        i += 1
    return count

x = 1
while True:
    triangle = x * (x + 1) // 2
    if count_divisors(triangle) > 500:
        print(triangle)
        break
    x += 1