import hashlib

w = open('after_change_hash.txt', 'w')
r = open('my_pass_list.txt', 'r')
l1 = []

for i in r:
    l1.append(i[:-1])

#print(l1)

for i in l1:
    w.write(hashlib.md5(i.encode()).hexdigest() + '\n')
