from math import factorial

digit_factorials = [factorial(i) for i in range(10)]
result = 0

for num in range(10, factorial(9) * 7):
    if sum(digit_factorials[int(d)] for d in str(num)) == num:
        result += num

print(result)