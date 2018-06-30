"""
Given a number n, find the n-th term in the series 1, 3, 6, 10, 15, 21…

Input:

The first line of input contains an integer T denoting the number of testcases. T test cases follow. Each test case contains an integer n.

Output:

Print the nth term

Constraints:

1<=T<=100

1<=n<=1000

Examples:

Input:

2
3
4

Output:

6
10
"""


def n_th_term_of_series(n):
    return n * (n + 1) // 2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(n_th_term_of_series(n))
