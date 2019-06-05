'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

--
Congratulations, the answer you gave to problem 10 is correct.

You are the 293210th person to have solved this problem.

You have earned 1 new award:

Decathlete: Solve ten consecutive problems

'''

from p0003 import prime_generator

lim = 2*10**6
sum = 0
print(lim)
for i, x in enumerate(prime_generator()):
    if x >lim:
        break
    sum += x
print(sum)