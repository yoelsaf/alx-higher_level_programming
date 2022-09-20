#!/usr/bin/python3
<<<<<<< HEAD
for i in range(0, 10):
    for j in range(0, 10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end='')
=======

for num in range(0, 9):
    for num_1 in range(1, 10):
        if num < num_1:
            if num == 8:
                print("{}{}".format(num, num_1))
            else:
                print("{}{},".format(num, num_1), end=" ")
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
