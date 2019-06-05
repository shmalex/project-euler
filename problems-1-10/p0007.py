'''
Congratulations, the answer you gave to problem 7 is correct.

You are the 376763rd person to have solved this problem.

This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 
'''

import numpy as np

from p0003 import prime_generator

for i, x in enumerate(prime_generator()):
    if i == 10001-1:
        print(x)
        break