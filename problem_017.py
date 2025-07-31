import inflect

p = inflect.engine()
total_letters = 0

for i in range(1, 1001):
    words = p.number_to_words(i)
    words = words.replace(" ", "").replace("-", "")
    total_letters += len(words)

print(total_letters)