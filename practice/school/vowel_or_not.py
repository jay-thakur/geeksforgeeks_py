"""
Write a program to check whether a character is vowel or not.

Input:

The first line of the input contains T denoting total number of testcases. Each of the testcase contains one character c.
Note : c is either lowercase or uppercase english aplhabetic character

Output:

Print "YES" if character is vowel else "NO". (without the quotes)

Constraints:

1<=T<=100


Example:

Input:
2
a
z

Output:
YES
NO
"""


def vowel_or_not(char):
    if char in ('a', 'e', 'i', 'o', 'u'):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        char = input()
        print(vowel_or_not(char))