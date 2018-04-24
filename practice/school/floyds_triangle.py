"""
Given an input n, print Floyd's triangle with n lines.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n.

Output:
Print the Floyd's triangle with n lines.

Constraints:
1<=T<=10
1<=N<=20

Example:

Input:
2
4
5

Output:
1
2 3
4 5 6
7 8 9 10
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""


def floyd_triangle(n):
    k = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(k, end=' ')
            k += 1
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        floyd_triangle(n)
