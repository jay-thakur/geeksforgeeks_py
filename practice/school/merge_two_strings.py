"""
Given two strings S1 and S2 as input, the task is to merge them alternatively.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two strings S1 and S2.

Output:
For each test case, print the merged string in new line.

Constraints:
1<=T<=100
1<=|strings length|<=104

Example:
Input:
2
Hello Bye
abc def

Output:
HBeylelo
adbecf
"""


def merge_two_strings(first_str, sec_str):
    for i, j in zip(first_str, sec_str):
        print(i + j, end='')

    p = min(len(first_str), len(sec_str))
    if len(first_str) < len(sec_str):
        print(sec_str[p:])
    else:
        print(first_str[p:])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        first_str, sec_str = input().split()
        merge_two_strings(first_str, sec_str)
