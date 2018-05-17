"""
Given a binary string of 0 and 1, write a program to check that the given string is valid or not. The given string is valid when there is no zero is present in between 1’s. For example, 1111, 0000111110, 1111000 are valid strings but 01010011, 01010, 101 are not.

Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. First line of each test case contains a binary string.

Output:
For each test case print "VALID" without quotes if the string is valid otherwise print "INVALID" without quotes if the string is invalid.

Constraints:
1<=T<=100
2<=length(Str)<=105

Example:
Input:
3
100
1110001
00011
Output:
VALID
INVALID
VALID
"""


def check_binary_string(str):
    str = str.strip("0")
    flag = "VALID"
    if '10' in str or '01' in str:
        flag = "INVALID"
    return flag


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(check_binary_string(str))
