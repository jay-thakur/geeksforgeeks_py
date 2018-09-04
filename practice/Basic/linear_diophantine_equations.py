"""
A Diophantine equation is a polynomial equation, usually in two or more unknowns, such that only the integral solutions are required. An Integral solution is a solution such that all the unknown variables take only integer values.

Given three integers a, b, c representing a linear equation of the form : ax + by = c. Determine if the equation has a solution such that x and y are both integral values.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains the integers a, b and c.

Output:

If the equation has possible integral solutions print 1 else print 0. Print the answer for each test case in a new line.


Constraints:

1<= T <=100

1<= a, b, c <=100000


Example:

Input:

1
3 6 9

Output:

1
"""


from math import gcd


def linear_diophantine_equations(a, b, c):
    if c % gcd(a, b) == 0:
        return 1
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b, c = [int(i) for i in input().split()][0:3]
        print(linear_diophantine_equations(a, b, c))
