file_tr = open('trigrams.txt', 'r')

trigrams = {}
list_trigrams_keys = []

for line in file_tr:
    temp_list = line.split(" ")
    trigrams[temp_list[0]] = temp_list[1]

for i in trigrams:
    list_trigrams_keys.append(i)

#print(trigrams)

def check_with_trigrams(string):
    dict_numbers = {}
    length_for_loops = len(string) - 2
    for i in range(length_for_loops):
        temp_3_symbols = string[i] + string[i+1] + string[i+2]
        for l in range(len(list_trigrams_keys)):
            trigram = list_trigrams_keys[l]
            if trigram == temp_3_symbols:
                print("ALSO YESS")
                dict_numbers[list_trigrams_keys[i]] = 1
                for k in range(i+1, length_for_loops):
                    print("K: ", k)
                    temp_3_symbols_2 = string[k] + string[k+1] + string[k+2]
                    if temp_3_symbols_2 == trigram:
                        print("YESS")
                        temp_val = 
                        dict_numbers[trigram] = dict_numbers[trigram] + 1
    print(dict_numbers)

#check_with_trigrams("EFFPQLEKVTVPCPYFLMVHQLUEWCNVWFYGHYTCETHQEKLPVMSAKSPVPAPVYWMVHQLUSPQLYWLASLFVWPQLMVHQLUPLRPSQLULQESPBLWPCSVRVWFLHLWFLWPUEWFYOTCMQYSLWOYWYETHQEKLPVMSAKSPVPAPVYWHEPPLUWSGYULEMQTLPPLUGUYOLWDTVSQETHQEKLPVPVSMTLEUPQEPCYAMEWWYTYWDLUULTCYWPQLSEOLSVOHTLUYAPVWLYGDALSSVWDPQLNLCKCLRQEASPVILSLEUMQBQVMQCYAHUYKEKTCASLFPYFLMVHQLUPQLHULIVYASHEUEDUEHQBVTTPQLVWFLRYGMYVWMVFLWMLSPVTTBYUNESESADDLSPVYWCYAMEWPUCPYFVIVFLPQLOLSSEDLVWHEUPSKCPQLWAOKLUYGMQEUEMPLUSVWENLCEWFEHHTCGULXALWMCEWETCSVSPYLEMQYGPQLOMEWCYAGVWFEBECPYASLQVDQLUYUFLUGULXALWMCSPEPVSPVMSBVPQPQVSPCHLYGMVHQLUPQLWLRPOEDVMETBYUFBVTTPENLPYPQLWLRPTEKLWZYCKVPTCSTESQPBYMEHVPETCMEHVPETZMEHVPETKTMEHVPETCMEHVPETT")
check_with_trigrams("NVNVBAMPNVNVNVAMPNVNWOWOWOWOOOWOWOOWOWOW")





