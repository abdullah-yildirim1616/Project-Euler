a, b = 1, 1
basamak = 0
sira=2
while basamak < 1000:
    a, b = b, a + b
    sira += 1
    basamak= len(str(b))

print(sira)