import base64
import operator

file = base64.b64decode("G0IFOFVMLRAPI1QJbEQDbFEYOFEPJxAfI10JbEMFIUAAKRAfOVIfOFkYOUQFI15ML1kcJFUeYhA4IxAeKVQZL1VMOFgJbFMDIUAAKUgFOElMI1ZMOFgFPxADIlVMO1VMO1kAIBAZP1VMI14ANRAZPEAJPlMNP1VMIFUYOFUePxxMP19MOFgJbFsJNUMcLVMJbFkfbF8CIElMfgZNbGQDbFcJOBAYJFkfbF8CKRAeJVcEOBANOUQDIVEYJVMNIFwVbEkDORAbJVwAbEAeI1INLlwVbF4JKVRMOF9MOUMJbEMDIVVMP18eOBADKhALKV4JOFkPbFEAK18eJUQEIRBEO1gFL1hMO18eJ1UIbEQEKRAOKUMYbFwNP0RMNVUNPhlAbEMFIUUALUQJKBANIl4JLVwFIldMI0JMK0INKFkJIkRMKFUfL1UCOB5MH1UeJV8ZP1wVYBAbPlkYKRAFOBAeJVcEOBACI0dAbEkDORAbJVwAbF4JKVRMJURMOF9MKFUPJUAEKUJMOFgJbF4JNERMI14JbFEfbEcJIFxCbHIJLUJMJV5MIVkCKBxMOFgJPlWOzKkfbF4DbEMcLVMJPx5MRlgYOEAfdh9DKF8PPx4LI18LIFVCL18BY1QDL0UBKV4YY1RDfXg1e3QAYQUFOGkof3MzK1sZKXIaOnIqPGRYD1UPC2AFHgNcDkMtHlw4PGFDKVQFOA8ZP0BRP1gNPlkCKw==")
print("pos 001 file after b64: ", file)
#new = []
#for k in file:
    #new.append(chr(operator.xor(k,k)))
#print("pos. 002 new after k xor k: ", new)
file_length = len(file)
list_after_xor = [[]]
for i in range (1, file_length - 1):
    temp_list = []
    for_first_string = 0
    for k in range(i, file_length):
        temp_list.append(chr(operator.xor(file[for_first_string], file[k])))
        for_first_string = for_first_string + 1
    for k in range(i):
        temp_list.append(chr(operator.xor(file[for_first_string], file[k])))
        for_first_string = for_first_string + 1
    list_after_xor.append(temp_list)

length_after_xor = len(list_after_xor[1])
counter_list = []
for i in range (2, 543):
    temp_counter = 0
    for k in range(length_after_xor):
        if list_after_xor[1][k] == list_after_xor[i][k]:
            temp_counter = temp_counter + 1
    counter_list.append(temp_counter)

print(counter_list)
