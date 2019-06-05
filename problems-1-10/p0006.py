
'''
Congratulations, the answer you gave to problem 6 is correct.

You are the 440782nd person to have solved this problem.

This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 

'''

import numpy as np

max = 100
nums = np.sum(np.array(range(max+1))**2)
sum = np.sum(range(max+1))**2
print(sum - nums)