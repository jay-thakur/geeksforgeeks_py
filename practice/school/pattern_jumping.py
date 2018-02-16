"""
Shaggy has a frog Akki. Akki is very hungry and Shaggy decides to feed it by playing a little game. Akki is a special frog which can jump as far as it wants but has a special pattern: He starts at the point 0.

In his first turn, he can make a jump of 1 unit. Now for all consequent turns, if the frog is currently at a distance x (from the start), his jump will take him x units forward. Given a leaf at a distance N , you have to find if the frog can reach that leaf or not.

Input

The first line contains number of test cases 'T' followed by 'T' non-negative integer 'x' denoting the distance.
Output:

Output contains T line containing,for each test cases True if the frog Akki can reach that pillar and print False otherwise.
Constraints:

1<=T<=100
1<=x<=10000

Example:

Input:

3
1
7
64

Output:

True
False
True
"""


def pattern_jumping(n):
    if n & (n - 1) == 0 and n != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(pattern_jumping(n))