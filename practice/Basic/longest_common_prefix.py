"""
Given two string str1 and str2(of lower case alphabets) of same length. Find the longest common prefix from str1 and str2.

NOTE: If there is no common prefix then print "-1".

INPUT: First line of the input is T denoting the number of test cases. Each test case takes two strings as input.

OUTPUT: Print the index from where the longest common prefix of str1 is found in str2 and the longest common prefix with a space in between.

CONSTRAINTS:
1<=T<=100
1<=Length of strings<10000

Examples:
INPUT:
2
geeks
dgeek
practicegeeks
coderpractice

OUTPUT:
1 geek
5 practice
"""


def longest_common_prefix(s1, s2):
    for i in range(len(s1)):
        s = s1[:len(s1) - i]
        if s in s2:
            print(s2.index(s), s)
            break
    else:
        print(-1)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()
        longest_common_prefix(s1, s2)
