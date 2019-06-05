''' 
https://projecteuler.net/problem=1

Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import numpy as np

def find_sum2(max_number, multipliers):
    ret = 0
    for x in range(1, max_number):
        for m in multipliers:
            if (x % m) == 0:
                ret += x
                break
    return ret

def find_sum(max_number, multipliers):
    ret = 0
    for multiplier in multipliers:
        max_mul = int(max_number / multiplier)
        for x in range(1, int(max_mul) + 1):
            nn = x*multiplier
            if (nn < max_number):
                ret += x*multiplier
    print('numbers below', max_number,
          'that are multiples of', multipliers, 'sum is', ret)
    # print(ret)
    return ret


if __name__ == "__main__":
    assert find_sum2(13, [3]) == (
        3+6+9+12), "find_sum2([3,5]) ==  "+str((3+6+9+12))
    assert find_sum2(10, [3, 5]) == (
        3+6+9+5), "find_sum2([3,5]) ==  " + str((3+6+9+5))
    assert find_sum2(15, [3, 5]) == (
        3+6+9+12+5+10), "find_sum2([3,5]) == " + str((3+6+9+12+5+10))
    print(find_sum2(1000, [3, 5]))
