'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Congratulations, the answer you gave to problem 4 is correct.

You are the 431800th person to have solved this problem.

This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 

'''
import numpy as np
import sys
sys.path.append('../')
from tools import dprint

def is_polyndor(s):
    return s[:3] == s[3:][::-1]

pols = []
for x in list(range(1,1000))[::-1]:
    for y in list(range(1,1000))[::-1]:
        if y < x:
            break
        dprint(x,y)
        if is_polyndor(str(x*y)):
            print(x,'*',y,'=',x*y)
            pols.append(x*y)

print(list(sorted(pols, reverse=True))[0])
