"""
Given a number n, count the total number of digits required to write all numbers from 1 to n.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n.

Output:
Print the total number of digits required to write all numbers from 1 to n.

Constraints:
1<=T<=10^5
1<=n<=10^5

Example:
Input:
2
13
4

Output:
17
4
"""


def total_digits(n):
    s = 0
    for i in range(0, len(str(n)) - 1):
        s += 9 * 10 ** i * (i + 1)
    a = 10 ** (len(str(n)) - 1) - 1
    s += (n - a) * len(str(n))
    return s


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(total_digits(n))
