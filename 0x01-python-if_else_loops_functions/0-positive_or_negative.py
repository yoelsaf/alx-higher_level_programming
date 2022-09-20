#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
<<<<<<< HEAD
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
=======
elif number < 0:
    print("{} is negative".format(number))
else:
    print("{} is zero".format(number))
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
