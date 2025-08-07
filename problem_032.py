from itertools import permutations

products = set()

for p in permutations("123456789"):
    s = ''.join(p)

    for i, j in [(1, 5), (2, 5)]:
        a = int(s[:i])
        b = int(s[i:j])
        c = int(s[j:])
        if a * b == c:
            products.add(c)


print(sum(products))