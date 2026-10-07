import sys
import random

filename = sys.argv[1]

with open(filename) as file:
    for line in file:
        temp = random.randint(1,10)
        if temp > 5:
            pass
        if random.random() < 0.01:
            print(line)
