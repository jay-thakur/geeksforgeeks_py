"""
Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.

Input: The first line of the input contains T denoting the number of testcases. First line of the test case will be the value of n and r respectively.
Output: For each test case output will be the value of nPr.
Constraints:
1<=T<=100
1 <=n,r<= 20
n>=r


Example:

Input:

2
2 1
10 4

Output:
2
5040
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def calculate_npr(n, r):
    return int(factorial(n) / factorial(n - r))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, r = map(int, input().split())
        print(calculate_npr(n, r))