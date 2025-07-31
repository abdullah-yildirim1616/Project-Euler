def collatz_chain_length(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        length += 1
    return length

max_length = 0
number = 0

for i in range(1, 1000000):
    length = collatz_chain_length(i)
    if length > max_length:
        max_length = length
        number = i

print(number)