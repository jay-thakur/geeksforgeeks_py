"""
Given two floating point numbers, find remainder.

INPUT : The first line consists of an integer T i.e. the number of test cases. First and last line of each test case consists of two double values a and b.

OUTPUT : Print the remainder of the two values.

CONSTRAINTS :
1<=T<=100
1<=a,b<=1000

EXAMPLES :
INPUT :
2
36.5 5.0
9.7 2.3

OUTPUT :
1.5
0.5
"""


def modulus_of_two_num(a, b):
    return round(a % b, 2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = [float(i) for i in input().split()][0:2]
        print(modulus_of_two_num(a, b))
