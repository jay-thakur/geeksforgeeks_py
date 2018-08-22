"""
Given N, check whether it is a Narcissistic number or not.

Note:Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.
Output:

Print 'Yes' if it is narcissistic,otherwise print 'No'.

Constraints:

1<=T<=100

1<=N<=100000
Example:

Input:
2
407
111

Output:
Yes
No

Explanation:
Testcase 1:- 4^3+0^3+7^3 = 64+0+343 = 407 equals to N.

Testcase 2:- 1^3+1^3+1^3 = 3 is not equal to N.
"""


def narcissistic_number(n):
    s = 0
    for i in range(len(str(n))):
        s = s + (int(str(n)[i])) ** (len(str(n)))

    if s == n:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(narcissistic_number(n))
