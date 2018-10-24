"""
Given a binary string, count number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.


Input:

The first line of input contains an integer T denoting the number of test cases.
Each test case consist of an integer 'n' denoting the string length and next line is followed by a binary string .

Output:

Print the number of substring starting and ending with 1 in a separate line.

Constraints:

1 ≤ T ≤ 40
1 ≤ |s| ≤ 1000


Example:

Input:
1
4
1111
Output:
6
"""


def binary_string(s):
    l = s.count('1')
    return l * (l - 1) // 2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()[0:n]
        print(binary_string(s))
