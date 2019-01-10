"""
Given a positive integer N, find the Nth fibonacci number. Since the answer can be very large, print the answer modulo 1000000007.

Input:

The first line of input contains T denoting the number of testcases.Then each of the T lines contains a single positive integer N.

Output:

Output the Nth fibonacci number.

Constraints:

1<=T<=200
1<=N<=1000

Example:

Input:
3
1
2
5

Output:
1
1
5
"""


def nth_fibonacci_number(n):
    f1 = 1
    f2 = 0

    for _ in range(n):
        f2 = f1 + f2
        f1 = f2 - f1
    return f2 % 1000000007


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(nth_fibonacci_number(n))
