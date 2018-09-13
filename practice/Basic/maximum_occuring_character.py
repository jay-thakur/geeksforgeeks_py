"""
Given a string, find the maximum occurring character in the string. If more than one character occurs maximum number of time then print the lexicographically smaller character.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case consist of a string in 'lowercase' only in a separate line.

Output:
Print the lexicographically smaller character which occurred the maximum time.

Constraints:
1 ≤ T ≤ 30
1 ≤ |s| ≤ 100

Example:

Input:
2
testsample
geeksforgeeks

Output:
e
e
"""


def max_occuring_char(s):
    frequencies = set((-s.count(c), c) for c in s)
    _, ans = min(frequencies)
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(max_occuring_char(s))
