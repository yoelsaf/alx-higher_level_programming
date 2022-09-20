#!/usr/bin/python3
def uppercase(str):
    for i in str:
<<<<<<< HEAD
        i = ord(i)
        if i >= 97 and i <= 122:
            i -= 32
        i = chr(i)
        print("{}".format(i), end='')
    print("")
=======
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(i) - (ord('a') - ord('A')))
        print("{:s}".format(i), end='')
    print()
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
