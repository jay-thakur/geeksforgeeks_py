"""
You are given a positive integer N and you have to find the number of non negative integral solutions to a + b + c = N.


Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
The first and only line of each test case contains a positive integer N.

Output:
For each test case in a new line, print the number of possible non negative integral solutions.


Constraints:
1 <= T <= 100
1 <= N <= 1000


Example:

Input:
2
10
20

Output:
66
231
"""


def number_of_integer_solutions(n):
    return int((n+1)*(n+2)/2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(number_of_integer_solutions(n))