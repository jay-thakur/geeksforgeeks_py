"""
Given the value of n, we need to find the sum of the series where i-th term is sum of first i natural numbers.

Note:- Sum of the series 1 + (1+2) + (1+2+3) + (1+2+3+4) + …… + (1+2+3+4+…+n)

Input:

The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows, a single line of the input containing a positive integer N.
Output:

Print the sum of the series of N terms for each testcase.
Constraints:

1<=T<=100

1<=N<=1000
Example:

Input:
2
5
10

Output:
35
220

Explanation:
Testcase 1:

(1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) = 35
Testcase 2:
(1) + (1+2) + (1+2+3) +  .... +(1+2+3+4+.....+10) = 220
"""


def special_series_sum(n):
    return ((n ** 3) + 3 * (n ** 2) + 2 * n) // 6


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(special_series_sum(n))
