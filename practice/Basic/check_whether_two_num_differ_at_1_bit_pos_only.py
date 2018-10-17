"""
Given two non-negative integers a and b. The problem is to check whether the two numbers differ at one bit position only or not.

Examples:

Input : a = 13, b = 9
Output : 1
(13)10 = (1101)2
(9)10 = (1001)2
Both the numbers differ at one bit position only, i.e,
differ at the 3rd bit from the right.

Input : a = 15, b = 8
Output : 0
INPUT : The first line contains an integer T i.e. the number of test cases.First and last line of each test case consists of two integers n and m.
OUTPUT : If given numbers n and m differ at single bit position then print "1" otherwise print "0".

CONSTRAINTS:
1<=T<=200
1<=n,m<=104

EXAMPLES:
INPUT:
1
13 9
OUTPUT:
1
"""


def if_teo_num_differ_at_one_bit(n, m):
    t = n ^ m
    if t & t - 1 == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()][0:2]
        print(if_teo_num_differ_at_one_bit(n, m))
