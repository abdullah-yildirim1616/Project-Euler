def check_polindrome(x):
    str_number = str(x)
    reverse_number = str_number[::-1]
    if str_number == reverse_number:
        return True
    else:
        return False
    
big_polindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        if check_polindrome(i*j) and i*j > big_polindrome:
            big_polindrome = i*j

print(big_polindrome)