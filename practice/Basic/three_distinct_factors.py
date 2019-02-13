"""
Given a positive integer N. The task is to check whether a number has exactly three distinct factors or not.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a number N as input.

Output:
For each test case, print "1" if the number has exactly three distinct factors else print "0".

Constraints:
1<=T<=500
1<=N<=1018

Example:
Input:
2
10
9

Output:
0
1
"""


def prime(sqt):
    j = 2
    while j <= sqt ** .5:
        if sqt % j == 0:
            return
        j = j + 1
    return 1


def three_distinct_factors(n):
    if n ** .5 == int(n ** .5):
        sqt = int(n ** .5)
        if prime(sqt):
            return "1"
        else:
            return "0"
    else:
        return "0"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(three_distinct_factors(n))
