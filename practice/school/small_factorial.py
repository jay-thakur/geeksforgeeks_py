"""
Calculate factorial of a given number N.

Input:

The first line contains an integer 'T' denoting the total number of test cases. In each test cases, it contains an integer 'N'.


Output:
In each separate line output the answer to the problem.

Constraints:

1<=T<=100
1<=N<=18


Example:
Input :
1
5

Output:

120
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(factorial(n))