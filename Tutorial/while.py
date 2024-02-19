from ast import If
from random import randint
import random

sum = 0

while True:
        random_number = random.randint(10, 30)
        print(random_number)

        sum += random_number

        if random_number == 15 or random_number == 25:
            break

print(sum)
