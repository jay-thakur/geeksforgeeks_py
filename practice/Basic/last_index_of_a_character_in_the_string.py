"""
Given a string S containing all the characters and a character X, the task is to find last index of X in string S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains a string S and the second line contains a character X.

Output:
For each test case, print the last index in new line, If X is not present in the string print "-1".

Constraints:
1<=T<=100
1<=|string length|<=105

Example:
Input:
2
Geeks
e
Hello world
o
Output:
2
7
"""


def last_index_of_a_character_in_the_string(s, x):
    s = s[::-1]
    if x in s:
        return len(s) - s.index(x) - 1
    else:
        return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        x = input()
        print(last_index_of_a_character_in_the_string(s, x))
