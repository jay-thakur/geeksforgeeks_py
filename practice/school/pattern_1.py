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


def print_pattern(n):
    ccode = 65
    for j in range(n):
        for k in range(n):
            if j == 0 or j == n - 1:
                print(chr(ccode), end="")
                ccode += 1
            else:
                if k == 0 or k == n - 1:
                    print(chr(ccode), end="")
                    ccode += 1
                else:
                    print("$", end="")
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print_pattern(n)
