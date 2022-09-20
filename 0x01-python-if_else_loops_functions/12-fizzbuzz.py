#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
<<<<<<< HEAD
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        else:
            print("{}".format(i), end=' ')
=======
        if (i % 5 == 0) and (i % 3 == 0):
            print('FizzBuzz ', end='')
        elif (i % 3 == 0):
            print('Fizz ', end='')
        elif (i % 5 == 0):
            print('Buzz ', end='')
        else:
            print('{} '.format(i), end='')
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
