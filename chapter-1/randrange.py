import random

highest = 10

while 1:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break