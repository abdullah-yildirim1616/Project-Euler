with open("0022_names.txt") as file:
    names = file.read().replace('"', '').split(',')

names.sort()

total_score = 0

for index, name in enumerate(names, start=1):
    name_score = sum(ord(char) - ord('A') + 1 for char in name)
    total_score += index * name_score

print(total_score)