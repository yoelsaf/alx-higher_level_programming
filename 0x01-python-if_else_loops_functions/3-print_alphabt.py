#!/usr/bin/python3
<<<<<<< HEAD
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{:c}".format(i), end='')
=======

for letter in range(ord('a'), ord('z') + 1):
    if letter != 113 and letter != 101:
        print('{}'.format(chr(letter)), end='')
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
