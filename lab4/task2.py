import hashlib
import csv
import uuid

file_to_read = open('my_pass_list.txt', 'r')
file_to_write = open('md5MyPasswords.txt', 'w')


def md5_cipher_csv ():
    file_to_write = "hashes_md5.csv"
    with open(file_to_write, 'w') as f:
        writer = csv.writer(f)
        for i in file_to_read:
            temp = hashlib.md5(i.encode()).digest()
            #print(temp)
            temp_list = [temp, "", ""]
            writer.writerow(temp_list)

def md5_cipher_txt ():
    for i in file_to_read:
        temp = hashlib.md5(i.encode()).hexdigest()
        file_to_write.write(temp + '\n')


def sha1_cipher ():
    file_to_write = "hashes_sha1.csv"
    with open(file_to_write, 'w') as f:
        writer = csv.writer(f)
        for i in file_to_read:
            salt = uuid.uuid4().hex
            temp = hashlib.sha1(salt.encode() + i.encode()).digest()
            # print(temp)
            temp_list = [temp, salt]
            writer.writerow(temp_list)

#sha1_cipher()
md5_cipher_txt()
