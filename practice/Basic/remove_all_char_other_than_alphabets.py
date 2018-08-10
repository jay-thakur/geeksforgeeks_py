"""
Given a string consisting of alphabets and others characters, the task is to remove all the characters other than alphabets and print the string so formed.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string S.

Output:
For each test case, print the remaining string in new line, If no character remains in the string print "-1".

Constraints:
1<=T<=100
1<=|string length|<=105

Example:
Input:
2
$Gee*k;s..fo, r'Ge^eks?
P&ra+$BHa;;t*ku, ma$r@@s#in}gh
Output:
GeeksforGeeks
PraBHatkumarsingh
"""


def remove_char_other_than_alphabets(s):
    st = ''
    for i in range(len(s)):
        if s[i].isalpha():
            st = st + s[i]

    if st == "":
        return -1
    else:
        return st


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(remove_char_other_than_alphabets(s))
