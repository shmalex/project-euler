''' 

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.

-
Congratulations, the answer you gave to problem 9 is correct.

You are the 320291st person to have solved this problem.

This problem had a difficulty rating of 5%. The highest difficulty rating you have solved remains at 5%. 
'''

a = 1
b = 1
sum = 1000

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = sum - a - b
        if ((a*a + b*b) ==(c*c)):
            print(a,b,c, a*b*c)
            exit()
