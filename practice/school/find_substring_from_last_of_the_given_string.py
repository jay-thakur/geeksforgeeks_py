"""
Given a string and a sub-string, your task is to find the last index of that sub-string that appears in the given String.
If the given sub-string doesn't appear in the string then print "-1".

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contain a sub-string S and a string S1.

Output:
For each test case in a new line print the required result.

Constraints:
1<=T<=100
1<=S, S1<=10000

Example:
Input:
2
geek
geeksforgeeks
abc
ababc

Output:
9
3
"""


def substring_from_last(first_str, second_str):
    i = second_str.rfind(first_str)
    return i + 1 if i >= 0 else -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        first_str = input()
        second_str = input()
        print(substring_from_last(first_str, second_str))