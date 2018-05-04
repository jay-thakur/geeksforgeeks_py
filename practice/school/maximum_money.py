"""
Given street of houses (a row of houses), each house having some amount of money kept inside; now there is a thief who is going to steal this money but he has a constraint/rule that he cannot steal/rob two adjacent houses. Find the maximum money he can rob.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N and money.

Output:

Print maximum money he can rob.

Constraints:

1 ≤ T ≤ 100
1 ≤ money ≤ 100
1 ≤ N ≤ 1000

Example:

Input:

2
5 10
2 12

Output:

30

12
"""


def maximum_money(n, m):
    return (int(n / 2) * m) if (n % 2 == 0) else (int(n / 2) + 1) * m


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()][0:2]
        print(maximum_money(n, m))
