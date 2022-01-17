from chromosome import  create_chromosome

number_of_chromosomes_in_population = 500


def create_population ():
    list_of_chromosomes = []
    for i in range(number_of_chromosomes_in_population):
        list_of_chromosomes.append(create_chromosome())
    return list_of_chromosomes

