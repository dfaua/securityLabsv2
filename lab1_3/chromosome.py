import random

list_correct_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']

def create_chromosome ():
    random.shuffle(list_correct_alphabet)
    #print(list_correct_alphabet)
    return (list_correct_alphabet)

create_chromosome()