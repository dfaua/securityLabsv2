file1 = open('61kENGwords.txt', 'r')

list_61k_common_words = []

for i in file1:
    if len(i) > 5:
        list_61k_common_words.append(i[:-1])

print(len(list_61k_common_words))