from itertools import islice

file_common_eng_words = open("resources/1000_most_common.txt")
list_common_words = []
for line in file_common_eng_words:
    list_common_words.append(line[:-1])

print(list_common_words)