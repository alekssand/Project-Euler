total = 0
for i in range(1,1001):
    total += i**i
word = str(total)
print(word[len(word)-10:])