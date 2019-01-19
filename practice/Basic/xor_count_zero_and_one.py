"""
Given a number N, the task is to find XOR of count of 0s and count of 1s in binary representation of a given number.

Input:

The first line of the testcase contains an integer T, denoting number of testcases. The next T lines contains one integer N each.
Output:

Print XOR of count of 0s and 1s in binary representation of the given number in separate lines


Constraints:

1<=T<=10^5

1<=N<=10^9


Example:

Input  : 5
Output : 3
Binary representation : 101
Count of 0s = 1,
Count of 1s = 2
1 XOR 2 = 3.

Input  : 7
Output : 3
Binary representation : 111
Count of 0s = 0
Count of 1s = 3
0 XOR 3 = 3.
"""


def xor_count_zero_and_count(n):
    ones = bin(n)[2:].count('1')
    zeros = bin(n)[2:].count('0')
    return ones ^ zeros


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(xor_count_zero_and_count(n))
