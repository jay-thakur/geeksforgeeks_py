"""
Given a string of a constant length, print a triangle out of it. The triangle should start with the first character of the string and keeps growing downwards by adding one character from the string.
The spaces on the left side of the triangle should be replaced with dot character.

Input:
First line of the input contains an integer T denoting the number of test cases. Then T test cases follow.  Each test case consists of a single line contaning a string of length N.

Output: Corresponding to each test case, a pattern of triangle is printed in N lines.

Constraints:
1 <=T<= 30
N= 5

Example:
Input:
2
geeks
thisi

Output:
....g
...ge
..gee
.geek
geeks
....t
...th
..thi
.this
thisi
"""


def triangle_growing_downwards(str):
    for i in range(1, len(str) + 1):
        print("." * int(len(str) - i) + str[0:i])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        triangle_growing_downwards(str)
