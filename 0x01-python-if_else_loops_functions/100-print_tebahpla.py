#!/usr/bin/python3
for i in range(122, 96, -1):
<<<<<<< HEAD
    if i % 2 != 0:
        print("{:c}".format(i - 32), end='')
    else:
        print("{:c}".format(i), end='')
=======
    if (i % 2 != 0):
        print('{}'.format(chr(i - 32)), end='')
    else:
        print('{}'.format(chr(i)), end='')
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
