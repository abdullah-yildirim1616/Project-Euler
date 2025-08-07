def is_palindrome(s):
    return s == s[::-1]

total = 0

for n in range(1, 1000000, 2):
    if is_palindrome(str(n)) and is_palindrome(bin(n)[2:]):
        total += n

print(total)