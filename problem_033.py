from math import gcd

numerator_product = 1
denominator_product = 1

for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        n_str = str(numerator)
        d_str = str(denominator)

        for digit in n_str:
            if digit in d_str and digit != '0':
                new_n_str = n_str.replace(digit, '', 1)
                new_d_str = d_str.replace(digit, '', 1)

                if new_d_str != '0' and new_n_str != '':
                    new_n = int(new_n_str)
                    new_d = int(new_d_str)

                    if new_d != 0 and numerator * new_d == denominator * new_n:
                        numerator_product *= numerator
                        denominator_product *= denominator

g = gcd(numerator_product, denominator_product)
print(denominator_product // g)