"""Given a natural number n, print 1 if it is perfect square else 0.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the number to be checked whether perfect square or not.

Output:
1 if it is perfect square else 0

Constraints:
1 <= T <= 30
1 <= N <= 100000

Example:
Input:
3
100
10
125

Output:
1
0
0
"""


import math


def check_if_perfect_square(n):
    num = int(math.sqrt(n))
    if num * num == n:
        return 1
    return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(check_if_perfect_square(n))