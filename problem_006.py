x = sum(range(1, 101))**2
print(x)
y = 0
for i in range(1, 101):
    y += i**2
print(y)

print(x - y)