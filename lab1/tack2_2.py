import base64
import operator

string = base64.b64decode("G0IFOFVMLRAPI1QJbEQDbFEYOFEPJxAfI10JbEMFIUAAKRAfOVIfOFkYOUQFI15ML1kcJFUeYhA4IxAeKVQZL1VMOFgJbFMDIUAAKUgFOElMI1ZMOFgFPxADIlVMO1VMO1kAIBAZP1VMI14ANRAZPEAJPlMNP1VMIFUYOFUePxxMP19MOFgJbFsJNUMcLVMJbFkfbF8CIElMfgZNbGQDbFcJOBAYJFkfbF8CKRAeJVcEOBANOUQDIVEYJVMNIFwVbEkDORAbJVwAbEAeI1INLlwVbF4JKVRMOF9MOUMJbEMDIVVMP18eOBADKhALKV4JOFkPbFEAK18eJUQEIRBEO1gFL1hMO18eJ1UIbEQEKRAOKUMYbFwNP0RMNVUNPhlAbEMFIUUALUQJKBANIl4JLVwFIldMI0JMK0INKFkJIkRMKFUfL1UCOB5MH1UeJV8ZP1wVYBAbPlkYKRAFOBAeJVcEOBACI0dAbEkDORAbJVwAbF4JKVRMJURMOF9MKFUPJUAEKUJMOFgJbF4JNERMI14JbFEfbEcJIFxCbHIJLUJMJV5MIVkCKBxMOFgJPlWOzKkfbF4DbEMcLVMJPx5MRlgYOEAfdh9DKF8PPx4LI18LIFVCL18BY1QDL0UBKV4YY1RDfXg1e3QAYQUFOGkof3MzK1sZKXIaOnIqPGRYD1UPC2AFHgNcDkMtHlw4PGFDKVQFOA8ZP0BRP1gNPlkCKw==")

print("decoded string: ", string)
#print("option 2: ", string)

list_string = list(string.split())
#for i in list_string:
    #print(i)

first_group = []
second_group = []
third_group = []

length = len(string)
for i in range(0, len(list_string), 3):
    first_group.append(list_string[i])
print(first_group)

for i in range(1, len(list_string), 3):
    second_group.append(list_string[i])
print(second_group)

for i in range(2, len(list_string), 3):
    third_group.append(list_string[i])
print(third_group)


def search_with_xor (input_list):
    for i in range(0, 255):
        temp_list = []
        for k in range(len(input_list)):
            #int_from_bytes = int.from_bytes(input_list[k], "big")
            #print(input_list[k], " --- XOR --- ", i)
            #print(int_from_bytes, " --- XOR --- ", i)
            #new = operator.xor(int_from_bytes, i)
            temp_str = input_list[k]
            print(temp_str)
            new = operator.xor(chr(i), temp_str.decode())
            #temp_list.append(new)
        print(temp_list)

search_with_xor(first_group)
search_with_xor(second_group)
search_with_xor(third_group)