word_count = {}

fhand = open("C:\Users\Josip\Desktop\skolovanje\OSU_LV\LV1\song.txt")
for line in fhand:
    line = line.rstrip()
    #print(line)
    words = line.split()
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count.update({word: 1})

fhand.close()
for x in word_count:
    if word_count[x] == 1:
        print(x)

print(word_count)
