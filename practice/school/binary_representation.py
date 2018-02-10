"""
Write a program to print Binary representation of a given number.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:

Print binary representation of a number in 14 bits.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 5000

Example:

Input:

2
2
5

Output:

00000000000010
00000000000101
"""


def binary_of(n):
    return "{0:014b}".format(n)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(binary_of(n))