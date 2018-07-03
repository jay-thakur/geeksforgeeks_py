"""
A number N is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120, …
Given a number N, the task is to print all factorial numbers smaller than or equal to N.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a number N as input.

Output:
For each test case, print all factorial numbers smaller than or equal to N in new line.

Constraints:
1<=T<=100
1<=N<=1018

Example:
Input:
2
2
6

Output:
1 2
1 2 6
"""


def fact(n):
    j = 1
    for k in range(1, 100):
        j = j * k
        if j > n:
            break
        print(j, end=' ')
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        fact(n)
