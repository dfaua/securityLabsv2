import random

list_correct_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']

str_correct_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number_of_populations = 5

def list_to_str(list):
    str = ""
    for i in list:
        str += i
    return str

def create_population ():
    population = []
    for i in range(number_of_populations):
        random.shuffle(list_correct_alphabet)
        #print("--", list_correct_alphabet)
        str = list_to_str(list_correct_alphabet)
        population.append(str)
    return (population)

#for i in create_population():
    #print(i)
