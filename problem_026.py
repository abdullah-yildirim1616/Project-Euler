def cycle_length(d):
    remainders = {}
    value = 1
    position = 0

    while value != 0:
        if value in remainders:
            return position - remainders[value]
        remainders[value] = position
        value = (value * 10) % d
        position += 1

    return 0

max_length = 0
result_d = 0

for d in range(2, 1000):
    length = cycle_length(d)
    if length > max_length:
        max_length = length
        result_d = d

print(result_d)