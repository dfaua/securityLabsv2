import hashlib
import csv
import uuid

file_to_read = open('my_pass_list.txt', 'r')
file_to_write = open('md5hashes.txt', 'w')


def md5_cipher ():
        for i in file_to_read:
            temp = hashlib.md5(i[:-1].encode()).hexdigest()
            file_to_write.write(temp + "\n")


def sha1_cipher ():
    file_to_write = "hashes_sha1.csv"
    with open(file_to_write, 'w') as f:
        writer = csv.writer(f)
        for i in file_to_read:
            salt = uuid.uuid4().hex
            temp = hashlib.sha1(salt[:-1].encode() + i[:-1].encode()).digest()
            # print(temp)
            temp_list = [temp, salt]
            writer.writerow(temp_list)

md5_cipher()
