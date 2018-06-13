"""
Given a single integer N, your task is to find the sum of the square of first N odd natural Numbers.

Examples:

Input : 3
Output : 35
12 + 32 + 52 = 35

Input : 8
Output : 680
12 + 32 + 52 + 72 + 92 + 112 + 132 + 152
Input:
First line of the input contains an integer T, denoting the number of test cases. Then T test case follows. The only line of each test case contains an integer N.

Output:
For each test case output the required anser on a new line.

Constraints:
1<=T<=100
N<=104

Example:
Input:
3
2
5
9
Output:

10
165
969
"""


def power_of_pow_odd_num(n):
    n = n - 1
    return (4 * n * (n + 1) * (2 * n + 1)) // 6 + 2 * n * (n + 1) + n + 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(power_of_pow_odd_num(n))
