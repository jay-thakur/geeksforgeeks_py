"""
For a given value N, denoting the number of Characters starting from the A, print reverse character bridge pattern.

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.
Output:

Print reverse character bridge pattern for each testcase.


Constraints:

1<=T<=50

1<=N<=26
Example:

Input:
2
5
8

Output:

ABCDEDCBA
ABCD  DCBA
ABC       CBA
AB            BA
A                 A
ABCDEFGHGFEDCBA
ABCDEFG GFEDCBA
ABCDEF   FEDCBA
ABCDE     EDCBA
ABCD       DCBA
ABC         CBA
AB           BA
A             A
"""
import string


def print_patter_for_reverse_char_bridge(n):
    l = string.ascii_uppercase
    for i in range(n):
        if i == 0:
            print(l[:n - i - 1] + ' ' * i + l[:n - i][::-1])
        else:
            print(l[:n - i] + ' ' * (2 * i - 1) + l[:n - i][::-1])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print_patter_for_reverse_char_bridge(n)
