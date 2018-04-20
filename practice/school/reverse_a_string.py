"""
Given a string S as input. You have to reverse the given string.

Input: First line of input contains a single integer T which denotes the number of test cases. T test cases follows, first line of each test case contains a string S.

Output: Corresponding to each test case, print the string S in reverse order.

Constraints:

1<=T<=100
3<= length(S) <=1000


Example:

Input:
3
Geeks
GeeksforGeeks
GeeksQuiz

Output:
skeeG
skeeGrofskeeG
ziuQskeeG
"""


def rev_str(str):
    return str[::-1]


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(rev_str(str))
