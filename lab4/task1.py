import time
import random
from itertools import islice

file_common_eng_words = open("resources/1000_most_common.txt")

def str_to_list(str):
    list = []
    for i in str:
        list.append(i)
    return  list

def real_unique_password():
    length_of_password = random.randint(8, 14)
    password = ""
    for i in range(length_of_password):
        rand_chr = chr(random.randint(48, 126))
        password += rand_chr
    return password

def mix_upped_lower_case(password_to_mix):
    temp_password = str_to_list(password_to_mix)
    length = len(temp_password)
    #for i in range(5):
        #temp_password.append(" ")
    for i in range(length):
        if random.randint(100, 10000) % 2 == 0:
            temp_letter = temp_password[i]
            if ord(temp_letter) >= 65 and ord(temp_letter) <= 90:
                temp_password.remove(temp_password[i])
                temp_password.insert(i, chr(ord(temp_letter) + 32))
            if ord(temp_letter) >= 97 and ord(temp_letter) <= 122:
                temp_password.remove(temp_password[i])
                temp_password.insert(i, chr(ord(temp_letter) - 32))
    return "".join([str(elem) for elem in temp_password])

def combine_words_from_file():
    password_length = random.randint(6, 10)
    password = ""
    temp = file_common_eng_words.read()
    temp = str.split(temp)
    while (len(password) <= password_length):
        rand_word = random.randint(0, len(temp) - 1)
        password += temp[rand_word]
    return password

def replace_letter_with_symbol(password):
    pass_list = str.split(password)


pas = real_unique_password()
print(pas)
print("mixed password: ", mix_upped_lower_case(pas))
print(combine_words_from_file())