"""
Write a program to find the simple interest for given principal amount P, time T(in years) and rate R.

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain three values P,T,R.

Output:
Print the simple interest

Constraints:
1<=T<=100
1<=P<=1000
1<=T<=20
1<=R<=20


Example:

Input:
2
42
8
15
501
10
5

Output:
50
250
"""


def calculate_simple_interest(p, t, r):
    return int((p*r*t)/100)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        p = int(input())
        t = int(input())
        r = int(input())
        print(calculate_simple_interest(p, t, r))