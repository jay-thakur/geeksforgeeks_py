"""
Given a number, the task is to check if it is tidy or not. A tidy number is a number whose digits are in non-decreasing order.

Examples:

Input : 1234
Output : Yes

Input : 1243
Output : No
Digits "4" and "3" violate the property.


Input:
The first line of input contains an integer T denoting the no of test cases. For each test case there will be single line containing an integer N.

Output:
For each test case in a new line print 1 if the no is a tidy number else print 0.

Constraints:
1 <= T <= 100
1 <= N <= 10^9+7

Example:
Input:
2
1234
1243
Output:
1
0
"""


def tidy_number(s):
    if list(s) == sorted(list(s)):
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(tidy_number(s))
