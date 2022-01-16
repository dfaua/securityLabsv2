from itertools import islice

file_common_eng_words = open("resources/1000_most_common.txt")
i = 0
string = ""
for line in file_common_eng_words:
    if i == 12:
        string = line
    i += 1

print(string)