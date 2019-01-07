"""
Given a string S consisting of lowercase latin letters, arrange all its letters in ascending order.

Input:

The first line of the input contains T denoting number of testcases.Then follows description of each testcase.The first line of the testcase contains positive integer N denoting the length of string.The second line contains the string S.

Output:
For each testcase,output the sorted string.

Constraints

1<=T<=100
1<=N<=100


Example:

Input:
1
5
edcab

Output:
abcde
"""


def sort_a_string(str):
    return ''.join(sorted(str))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        size = int(input())
        str = input()
        print(sort_a_string(str))
