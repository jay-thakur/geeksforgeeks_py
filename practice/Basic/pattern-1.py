"""
Pattern would look like this if, N=6
 ABCDEF
 G$$$$H
 I$$$$J
 K$$$$L
 M$$$$N
 OPQRST

Input:
First line consists of T test cases. Only line of every test case consists of an integer N.

Output:
Print the following pattern.

Constraints:
1<=T<=6
1<=N<=6

Example:
Input:
1
6
Output:
ABCDEF
G$$$$H
I$$$$J
K$$$$L
M$$$$N
OPQRST
"""


def pattern_1(n):
    ch = 'A'
    for i in range(n):
        print(ch, end='')
        ch = chr(ord(ch) + 1)
    print()
    for i in range(n - 2):
        print(ch, '$' * (n - 2), chr(ord(ch) + 1), sep='')
        ch = chr(ord(ch) + 2)
    if n != 1:
        for i in range(n):
            print(ch, end='')
            ch = chr(ord(ch) + 1)
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        pattern_1(n)
