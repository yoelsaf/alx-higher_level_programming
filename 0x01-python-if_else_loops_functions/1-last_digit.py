#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD

if number < 0:
    num = number * -1
    num = num % 10
    num = num * -1
else:
    num = number % 10
print("Last digit of {}".format(number), end=' ')
if num > 5:
    print("is {} and is greater than 5".format(num))
elif num == 0:
    print("is {} and is 0".format(num))
elif num < 6 and num != 0:
    print("is {} and is less than 6 and not 0".format(num))
=======
num = abs(number) % 10
if number < 0:
    num = -num
print("Last digit of {} is {} and is ".format(number, num), end="")
if num > 5:
    print("greater than 5")
elif num == 0:
    print("0")
else:
    print("less than 6 and not 0")
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
