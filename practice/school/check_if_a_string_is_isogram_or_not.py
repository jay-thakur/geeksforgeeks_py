"""
Given a word or phrase, check if it is isogram or not. An Isogram is a word in which no letter occurs more than once.

Input:

The first line of input contains an integer T denoting the number of test cases. Each test case consist of one strings in 'lowercase' only, in a separate line.
Output:

Print 1 if string is Isogram else print 0.
Constraints:

1 <= T <= 100

1 <= |S| <= 100
Example:

Input:

2
machine
geeks

Output:

1
0

Explanation:
For testcase 2: geeks is not an isogram as 'e' appears twice. Hence we print 0.
"""


def if_string_is_isogram(str):
    for c in str:
        if str.count(c) > 1:
            return 0
    else:
        return 1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        print(if_string_is_isogram(str))
