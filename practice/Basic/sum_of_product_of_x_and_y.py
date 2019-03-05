"""
Given a positive integer n. The task is to find the sum of product of x and y such that floor(n/x) = y .

Examples:

Input : n = 5
Output : 21
Following are the possible pairs of (x, y):
(1, 5), (2, 2), (3, 1), (4, 1), (5, 1).
So, 1*5 + 2*2 + 3*1 + 4*1 + 5*1
   = 5 + 4 + 3 + 4 + 5
   = 21.

Input : n = 10
Output : 87


Input:
The first line of input contains an integer T. The T test cases follow . Each test case contains an integer N.

Output:
For each test case in a new line print the required output.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
5
10

Output:
21
87
"""


def sum_of_product(n):
    res = 0
    for i in range(1, n + 1):
        res += n // i * i
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(sum_of_product(n))
