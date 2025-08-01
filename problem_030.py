total = 0

for number in range(2, 354295):
    digits = str(number)
    sum_of_powers = sum(int(d)**5 for d in digits)
    if sum_of_powers == number:
        total += number

print(total)