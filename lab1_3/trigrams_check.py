file_tr = open('trigrams.txt', 'r')

trigrams = {}

for line in file_tr:
    temp_list = line.split(" ")
    trigrams[temp_list[0]] = temp_list[1]


