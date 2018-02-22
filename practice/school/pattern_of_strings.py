"""
Given a string of length N, print a pattern of strings with first line being the given string of length n and keep priting in new line the strings in decreasing order of length till you print the single first character of the given string.

Input: First line of the input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consist of only one line which contains a string of length N.

Output:  Corresponding to each test case, pattern is printed in a new line.

Constraints:
1 <=T<= 30
N= 5

Example:

Input:
2
Geeks
th%ik

Output:
Geeks
Geek
Gee
Ge
G
th%ik
th%i
th%
th
t
"""


def pattern_of_strings(str):
    for i in range(len(str), 0, -1):
        print(str[:i])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input()
        pattern_of_strings(str)