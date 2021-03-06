"""
Given a natural number n, print all distinct divisors of it including 1 and the number itself.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the number whose divisors are to be printed.

Output:
All the divisors of the given number including 1 and the number itself are displayed in a line with a single space between them in an increasing order.

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
1 2 4 5 10 20 25 50 100
1 2 5 10
1 5 25 125
"""


def all_divisors_of(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
    print('')


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        all_divisors_of(n)