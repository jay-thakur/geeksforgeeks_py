"""
Given a single integer N, your task is to find the sum of the square of first N even natural Numbers.

Examples:

Input : 3
Output : 56
22 + 42 + 62 = 56

Input : 8
Output : 816
22 + 42 + 62 + 82 + 102 + 122 + 142 + 162
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
20
220
1140
"""


def power_of_pow_even_num(n):
    return (n * (n + 1) * (2 * n + 1) // 6) * 4


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(power_of_pow_even_num(n))
