"""
Given a string of a constant length, print a triangle out of it. The triangle should start with the given string and keeps shrinking downwards by removing one character from the begining of the string.
The spaces on the left side of the triangle should be replaced with dot character.

Input: First line of the input contains an integer T denoting the number of test cases. Then T test cases follow.  Each test case consists of a single line contaning a string of length N.

Output: Corresponding to each test case, a pattern of triangle is printed in N lines.

Constraints:
1 <=T<= 30
N= 5
Example:
Input:
2
Geeks
@io30

Output:
Geeks
.eeks
..eks
...ks
....s
@io30
.io30
..o30
...30
....0
"""


def triangle_shrinking_downwards(str):
    for i in range(len(str)):
        print('.' * i + str[i:])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        triangle_shrinking_downwards(str)