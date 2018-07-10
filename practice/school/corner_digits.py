"""
Given a number N and the task is to print the first and last digit of N.

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.
Output:

For each testcase, print a single line containing the first and last digit of N respectively.


Constraints:

1<=T<=100

1<=N<=100000
Example:

Input:

2
12345
98562

Output:

1 5
9 2

Explanation:
For testcase 1:  First digit of 12345 is 1 and last is 5.

For testcase 2: First digit of 98562 is 9 and last is 2.
"""


def corner_digits(n):
    return n[0], n[-1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        print(*corner_digits(n))
