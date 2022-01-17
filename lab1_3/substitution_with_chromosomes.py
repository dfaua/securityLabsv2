from population import create_population

list_correct_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']

text_to_decrypt = "EFFPQLEKVTVPCPYFLMVHQLUEWCNVWFYGHYTCETHQEKLPVMSAKSPVPAPVYWMVHQLUSPQLYWLASLFVWPQLMVHQLUPLRPSQLULQESPBLWPCSVRVWFLHLWFLWPUEWFYOTCMQYSLWOYWYETHQEKLPVMSAKSPVPAPVYWHEPPLUWSGYULEMQTLPPLUGUYOLWDTVSQETHQEKLPVPVSMTLEUPQEPCYAMEWWYTYWDLUULTCYWPQLSEOLSVOHTLUYAPVWLYGDALSSVWDPQLNLCKCLRQEASPVILSLEUMQBQVMQCYAHUYKEKTCASLFPYFLMVHQLUPQLHULIVYASHEUEDUEHQBVTTPQLVWFLRYGMYVWMVFLWMLSPVTTBYUNESESADDLSPVYWCYAMEWPUCPYFVIVFLPQLOLSSEDLVWHEUPSKCPQLWAOKLUYGMQEUEMPLUSVWENLCEWFEHHTCGULXALWMCEWETCSVSPYLEMQYGPQLOMEWCYAGVWFEBECPYASLQVDQLUYUFLUGULXALWMCSPEPVSPVMSBVPQPQVSPCHLYGMVHQLUPQLWLRPOEDVMETBYUFBVTTPENLPYPQLWLRPTEKLWZYCKVPTCSTESQPBYMEHVPETCMEHVPETZMEHVPETKTMEHVPETCMEHVPETT"
length_of_cipher = len(text_to_decrypt)
number_of_populations = 6

def substitution_with_alphabets ():
    temp_dict = {}
    chromosome = []
    for population_counter in range(number_of_populations):
        list_of_new_strings = []
        population = create_population()
        print("2342 population: ", population)
        for k in range(len(population)):
            new_string = ""
            chromosome_str = population[k]
            print(chromosome_str)
            for i in range (26):
                temp_dict[chromosome_str[i]] = list_correct_alphabet[i]
            print(temp_dict)
            for i in range(length_of_cipher):
                new_string += temp_dict[text_to_decrypt[i]]
            print(new_string)
            list_of_new_strings.append(new_string)
        for i in list_of_new_strings:
            pass




substitution_with_alphabets()
