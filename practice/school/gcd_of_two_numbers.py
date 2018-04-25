"""
Given two numbers, find the GCD of those 2 numbers.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two space separated integers a and b.

Output:
Print the GCD of the two numbers.

Constraints:
1 <= T <= 100
1 <= a , b <= 1000

Example:
Input:
98 56
48 18
Output:
14
6
"""


def gcd(a, b):
    if a == 0 or b == 0:
        return 0

    if a == b:
        return a

    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = [int(i) for i in input().split()][0:2]
        print(gcd(a, b))
