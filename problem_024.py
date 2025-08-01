import itertools

digits = '0123456789'

perms = itertools.permutations(digits)

for i, p in enumerate(perms, start=1):
    if i == 1000000:
        print(''.join(p))
        break