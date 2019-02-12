"""
Given an integer N, find the number of ways we can choose 3 numbers from {1,2,3…,N} such that their sum is even.

Input:-
The first line of the test case contains an integer T denoting number of test cases. Following T line contains an integer N each.

Output:-
Print the answer under modulo 109+7.

Constraints:-

1 <= T <= 4.5*103
3 <= N <= 106

Example:-
Input:-
2
3
4
Output:-
1
2

Explanation:
Testcase 1:For N=3 the only possible combination is {1,2,3}.So, the output is 1.
"""


def three_number_even_sum(n):
    odd = n // 2 + n % 2
    even = n // 2
    MOD = 10 ** 9 + 7
    return (even * (even - 1) * (even - 2) // 6 + odd * (odd - 1) // 2 * even) % MOD


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(three_number_even_sum(n))
