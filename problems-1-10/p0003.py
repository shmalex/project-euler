'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


You are the 487344th person to have solved this problem.

You have earned 1 new award:

Baby Steps: Solve three problems


This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 

'''
import numpy as np
import sys
import time
sys.path.append('../')
from tools import dprint

class prime_generator(object):
    primes = [2, 3, 5, 7, 11]
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def _next_prime(self):
        prime = prime_generator.primes[-1]
        while True:
            prime+=2
            if prime % 5 == 0:
                continue
            if is_prime(prime):
                return prime

    def next(self):
        if self.i == len(prime_generator.primes):
            dprint('get new prime')
            prime_generator.primes.append(self._next_prime())
        self.i+=1
        return prime_generator.primes[self.i-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def lpf(max):
    if max == 1:
        return None
    dprint('max', max)
    for prime in prime_generator():
        dprint('prime', prime)
        if max % prime == 0:
            yield prime
            yield from lpf(int(max / prime))
            break
        if prime > max:
            break
    return None
if __name__ == "__main__":
    print('*'.join([str(primes) for primes in lpf(100)]))