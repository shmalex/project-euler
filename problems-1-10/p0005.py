'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Congratulations, the answer you gave to problem 5 is correct.

You are the 438001st person to have solved this problem.

This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 


'''
from p0003 import prime_generator
from p0003 import lpf

import numpy as np

gen = prime_generator()
prims = []

MAX=100
while True:
    p = next(gen)
    if p>MAX:
        break
    prims.append(p)
print(prims)
big_nr = np.prod(prims)
print(np.prod(prims))



# 232792560
additionals = []
while True:
    new_big_nr = np.prod(additionals + [big_nr])
    rem = []
    for i in range(2, MAX+1):
        if ( new_big_nr % i != 0):
            print(new_big_nr, '%',i,'=', new_big_nr % i)
            rem.append(new_big_nr % i)
    if len(rem) == 0:
        print(new_big_nr)
        exit()
    else:
        # break reminder to least prime factors and take min
        try:
            listlpf = list(lpf(np.min(rem)))
            additionals.append(np.min(listlpf))
        except ValueError as identifier:
            print('>>>>',rem)
            raise identifier
        print(additionals)