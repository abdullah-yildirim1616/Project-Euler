def prime_check(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False       
    return True


counter = 0
number = 1
while counter < 10001:
    number += 1
    if prime_check(number):
        counter += 1
    

print(number)