import base64
import operator

string = base64.b64decode("G0IFOFVMLRAPI1QJbEQDbFEYOFEPJxAfI10JbEMFIUAAKRAfOVIfOFkYOUQFI15ML1kcJFUeYhA4IxAeKVQZL1VMOFgJbFMDIUAAKUgFOElMI1ZMOFgFPxADIlVMO1VMO1kAIBAZP1VMI14ANRAZPEAJPlMNP1VMIFUYOFUePxxMP19MOFgJbFsJNUMcLVMJbFkfbF8CIElMfgZNbGQDbFcJOBAYJFkfbF8CKRAeJVcEOBANOUQDIVEYJVMNIFwVbEkDORAbJVwAbEAeI1INLlwVbF4JKVRMOF9MOUMJbEMDIVVMP18eOBADKhALKV4JOFkPbFEAK18eJUQEIRBEO1gFL1hMO18eJ1UIbEQEKRAOKUMYbFwNP0RMNVUNPhlAbEMFIUUALUQJKBANIl4JLVwFIldMI0JMK0INKFkJIkRMKFUfL1UCOB5MH1UeJV8ZP1wVYBAbPlkYKRAFOBAeJVcEOBACI0dAbEkDORAbJVwAbF4JKVRMJURMOF9MKFUPJUAEKUJMOFgJbF4JNERMI14JbFEfbEcJIFxCbHIJLUJMJV5MIVkCKBxMOFgJPlWOzKkfbF4DbEMcLVMJPx5MRlgYOEAfdh9DKF8PPx4LI18LIFVCL18BY1QDL0UBKV4YY1RDfXg1e3QAYQUFOGkof3MzK1sZKXIaOnIqPGRYD1UPC2AFHgNcDkMtHlw4PGFDKVQFOA8ZP0BRP1gNPlkCKw==")

print("decoded string: ", string)
#print("option 2: ", string)
length_of_text = len(string)
int_result1 = 0
int_result2 = 0
int_result3 = 0
string_result1 = ""
string_result2 = ""
string_result3 = ""

def search_for_english (check_result):
    lenght = len(check_result)
    counter = 0
    for i in range(lenght):
        if check_result[i] >= "a":
            if check_result[i] <= "z":
                counter = counter + 1
    return counter

for i in range(255):
    result1 = ""
    result2 = ""
    result3 = ""
    for k in range(length_of_text):
        if k % 3 == 0:
            result1 = result1 + chr((operator.xor(string[k], i)))
    if i == 76:
        string_result1 = result1
        #print("pos 229: result1: ", result1)
    #temp1 = search_for_english(result1)
    #if temp1 > int_result1:
       # int_result = temp1
       # string_result1 = result1
    #print("i: ", i, " result1: ", result1)
    for k in range(1, length_of_text):
        if (k - 1) % 3 == 0:
            result2 = result2 + chr((operator.xor(string[k], i)))
    if i == 48:
        string_result2 = result2
        #print("pos 230: result2: ", result1)
        #temp2 = search_for_english(result2)
        #if temp2 > int_result2:
            #int_result = temp2
            #string_result2 = result2
    #print("i: ", i, " result2: ", result2)
    for k in range(2, length_of_text):
        if (k + 1) % 3 == 0:
            result3 = result3 + chr((operator.xor(string[k], i)))
        #temp3 = search_for_english(result3)
        #if temp3 > int_result3:
            #int_result = temp3
            #string_result3 = result3
    if i == 108:
        string_result3 = result3
    #print("i: ", i, " result3: ", result3)



print("1:", len(string_result1))
print("2:", len(string_result2))
print("3:", len(string_result3))
final_phrase = ""
for i in range (0, 181):
    final_phrase += string_result1[i]
    final_phrase += string_result2[i]
    final_phrase += string_result3[i]

final_phrase += string_result1[181]

print(final_phrase)

