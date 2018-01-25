"""
Write a Program to calculate the sum of n terms of a Geometric Progression when first term a and common ratio r is given.

Input:
The first line of the input contains T denoting the number of testcases. The first line of the test case will be the number of terms of GP and second line its first term and common ratio.

Output:
For each test case the output will be the sum of n terms of GP.

Constraints:

1 <= T<= 100
1 <= N <= 100
1 <= a,r <= 100

Example:

Input:

1
3
3 2

Output:

21.000000
"""


def sum_of_GP(n, a, r):
    if r == 1:
        return a * n
    else:
        return a * (1 - (r ** n)) / (1 - r)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a, r = map(int, input().split())
        print(sum_of_GP(n, a, r))