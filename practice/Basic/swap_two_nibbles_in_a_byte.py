"""
Given a byte, swap the two nibbles in it. For example 100 is be represented as 01100100 in a byte (or 8 bits). The two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.

Input:
The first line contains 'T' denoting the number of testcases. Each testcase contains a single positive integer X.

Output:
In each separate line print the result after swapping the nibbles.

Constraints:

1 ≤ T ≤ 70
1 ≤ X ≤ 255

Example:

Input:

2
100
129

Output:

70
24
"""


def swap_two_nibbles_in_a_byte(n):
    b = bin(n)[2:]
    b = (8 - len(b)) * '0' + b
    ans = b[4:] + b[:4]
    return int(ans, 2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(swap_two_nibbles_in_a_byte(n))