import sys
import random

filename = sys.argv[1]

with open(filename) as file:
    for line in file:
        item = random.choice(['A', 'B', 'C'])
        if item == 'A':
            pass
        if random.random() < 0.01:
            print(line)
