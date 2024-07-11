words_to_count = ["example", "all", "word", "up", "did", "him"]

words_counts = {word: 0 for word in words_to_count}

with open('peterrabbit.txt', 'r') as file:
    text = file.read().lower()

for word in words_to_count:
    words_counts[word] = text.count(word)


for word, count in words_counts.items():
    print(f"The word {word} appears {count} times in text.")
