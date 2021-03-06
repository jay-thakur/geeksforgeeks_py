"""
Given a string , write a program to title case every first letter of words in string.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case consists of a string s.

Output:
Print the required output.

Constraints:
1<=T<=100
1<=|Length of string|<=1000

Example:
Input:
1
I love programming

Output:
I Love Programming
"""


def upper_case_conversion(s):
    return s.title()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(upper_case_conversion(s))
