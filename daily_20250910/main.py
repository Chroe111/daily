import re

with open("input.txt") as f:
    text = f.read()

word_list = re.sub(r"[!\?\.,\n]", "", text.lower()).split(" ")

word_counts = {}
for word in word_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_word_counts = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))

for i, (word, count) in enumerate(sorted_word_counts.items()):
    if i == 10:
        break
    print(f"{word}: {count}")
