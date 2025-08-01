total = 1
number = 1

for size in range(3, 1002, 2):
    step = size - 1
    for _ in range(4):
        number += step
        total += number

print(total)