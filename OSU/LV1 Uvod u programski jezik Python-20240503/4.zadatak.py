word_count = {}

song = open("LV1 Uvod u programski jezik Python-20240503\song.txt")
for line in song:
    words = line.strip().split(" ")
    for word in words:
        if word not in word_count:
            word_count[word] = 1
            continue
        word_count[word] = word_count[word] + 1
song.close()
unique_words = 0
print(word_count)
for word in word_count:
    if word_count[word] == 1:
        unique_words += 1
        print(f"{word} : {word_count[word]}")
print(unique_words)