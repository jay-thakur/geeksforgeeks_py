"""
Given a string s, find the number of pairs of characters that are same. Pairs (s[i], s[j]), (s[j], s[i]), (s[i], s[i]), (s[j], s[j]) should be considered different.

INPUT: The first line consists of an integer T i.e. the number of test cases. Each test case has the single line input, denoting the string s.

OUTPUT: Print the total number of pairs in the string.

CONSTRAINTS:
1<=T<=100
1<=|Length of string|<=105

EXAMPLES:
INPUT :
2
air
geeksforgeeks

OUTPUT :
3
31

EXPLANATION:

Input: air
Output: 3
Explanation :
3 pairs that are equal are (a, a), (i, i) and (r, r)

Input : geeksforgeeks
Output : 31
"""


def no_of_equal_pairs(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1

    sums = 0
    for key, val in d.items():
        sums += (val * val)
    return sums


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(no_of_equal_pairs(s))
