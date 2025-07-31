number = 2**1000
digits = str(number)
digit_sum = sum(int(digit) for digit in digits)
print(digit_sum)