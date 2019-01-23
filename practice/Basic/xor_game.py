"""
Given a positive number k, we need to find a minimum value of positive integer n, such that XOR of n and n+1 is equal to k. If no such n exist then print -1.

Input:
The first line consists of an integer T i.e number of test cases. The only line of each test case consists of an integer k.

Output:
Print the required output.

Constraints:
1<=T<=100
1<=k<=100

Example:
Input:
2
3
6

Output:
1
-1
"""


def xor_game(n):
    for i in range(1, 101):
        j = i
        if (j ^ (j + 1)) == n:
            return j
    return -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(xor_game(n))
